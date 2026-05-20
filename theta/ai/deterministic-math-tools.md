# Deterministic Math Tool Surface (DRAFT 0.1)

**Status: DRAFT 2026-05-20.** Function signatures for the
deterministic-math tools the LLM coach is allowed to call. The
coach never computes numbers itself; it calls these tools and
narrates the output in voice. Required by `DESIGN.md §2.5 B` and
`PEDAGOGY.md §3.2`.

**Why deterministic**: math hallucination is the one class of
LLM error that (a) breaks user trust catastrophically and
(b) creates §206(4) anti-fraud exposure. Pricing, Greeks, P&L,
and breakevens are all closed-form (or near-closed-form)
calculations. They should run in code, not in a language model.

**Data tier**: 15-minute-delayed throughout (`DESIGN.md §2.5 D`).
No real-time data inside [PRODUCT]. All quote / chain functions
return delayed values and tag the timestamp.

**Schema format**: JSON schema for inputs and outputs. Tool names
in `snake_case`. Suitable for Claude function-calling, OpenAI tool
use, or any equivalent system.

---

## Market data tools

### `get_quote`
Get a 15-min-delayed quote for an equity or ETF.
```
inputs:
  ticker: string             # e.g., "NVDA"
  asof: timestamp | null     # null = latest available
outputs:
  ticker: string
  last: number
  bid: number
  ask: number
  volume: integer
  asof: timestamp            # actual delayed timestamp
  delay_minutes: integer     # always 15 under bootstrap
```

### `get_options_chain`
Get the delayed options chain for an underlying at a given
expiration.
```
inputs:
  ticker: string
  expiration: date           # e.g., "2026-06-20"
  asof: timestamp | null
outputs:
  ticker: string
  expiration: date
  underlying_price: number
  calls: array[
    {strike, bid, ask, mid, last, volume, open_interest, iv, delta, gamma, theta, vega}
  ]
  puts: array[
    {strike, bid, ask, mid, last, volume, open_interest, iv, delta, gamma, theta, vega}
  ]
  asof: timestamp
  delay_minutes: integer
```

### `list_expirations`
List available expirations for an underlying.
```
inputs:
  ticker: string
outputs:
  ticker: string
  expirations: array[date]
```

### `get_iv_rank`
IV rank: where current implied volatility sits within its
trailing N-day range (0 = bottom of range, 100 = top of range).
```
inputs:
  ticker: string
  lookback_days: integer = 252
  asof: timestamp | null
outputs:
  ticker: string
  iv_rank: number            # 0–100
  current_iv: number         # decimal, e.g., 0.32
  range_low: number
  range_high: number
  asof: timestamp
```

### `get_iv_percentile`
IV percentile: what fraction of days in the trailing N-day window
had IV at or below current.
```
inputs:
  ticker: string
  lookback_days: integer = 252
  asof: timestamp | null
outputs:
  ticker: string
  iv_percentile: number      # 0–100
  current_iv: number
  asof: timestamp
```

### `get_historical_iv`
Time series of historical implied volatility.
```
inputs:
  ticker: string
  start_date: date
  end_date: date
outputs:
  ticker: string
  series: array[{date, iv}]
```

### `get_earnings_date`
Next scheduled earnings date for an underlying.
```
inputs:
  ticker: string
outputs:
  ticker: string
  next_earnings: date | null
  confirmed: boolean
  bmo_amc: enum["BMO", "AMC", "unknown"]   # before/after market
```

### `get_dividend_dates`
Upcoming ex-dividend dates.
```
inputs:
  ticker: string
outputs:
  ticker: string
  next_ex_div: date | null
  amount: number | null
```

---

## Options pricing + Greeks

### `price_option`
Black-Scholes price for a single European option (or American
binomial for early-exercise-sensitive cases).
```
inputs:
  underlying_price: number
  strike: number
  days_to_expiration: integer
  iv: number                  # decimal
  risk_free_rate: number      # decimal, e.g., 0.045
  dividend_yield: number = 0
  option_type: enum["call", "put"]
  exercise_style: enum["european", "american"] = "european"
outputs:
  price: number
  intrinsic: number
  extrinsic: number
```

### `compute_greeks`
All five Greeks for a single option.
```
inputs: (same as price_option)
outputs:
  delta: number
  gamma: number
  theta: number               # per-day
  vega: number                # per 1% IV change
  rho: number                 # per 1% rate change
```

---

## Strategy structure tools

### `compute_strategy_payoff`
P&L profile of a multi-leg strategy at a given evaluation date.
```
inputs:
  underlying_price: number    # current
  legs: array[
    {
      side: enum["buy", "sell"],
      quantity: integer,
      type: enum["call", "put", "stock"],
      strike: number | null,        # null for stock
      premium: number,              # per share (per contract / 100)
      expiration: date | null
    }
  ]
  eval_date: date              # date to evaluate P&L at
  price_range: {min, max, steps}  # underlying prices to evaluate
outputs:
  payoff: array[{underlying_price, pnl}]
  max_profit: number | "unbounded"
  max_loss: number | "unbounded"
  breakevens: array[number]
  net_credit_or_debit: number  # positive = credit, negative = debit
```

### `compute_breakevens`
Just the breakevens for a multi-leg strategy.
```
inputs:
  legs: (same as compute_strategy_payoff)
outputs:
  breakevens: array[number]
```

### `compute_max_profit_loss`
Just max profit and max loss.
```
inputs:
  legs: (same as compute_strategy_payoff)
outputs:
  max_profit: number | "unbounded"
  max_loss: number | "unbounded"
  defined_risk: boolean
```

### `compute_probability_profit`
Probability that the strategy expires profitable, using
implied-volatility-derived distribution.
```
inputs:
  legs: (same as compute_strategy_payoff)
  underlying_price: number
  iv: number
  days_to_expiration: integer
outputs:
  pop: number                  # 0–1
  method: string               # e.g., "black-scholes lognormal"
```

### `compute_probability_touch`
Probability the underlying touches a given strike before expiry.
```
inputs:
  underlying_price: number
  strike: number
  days_to_expiration: integer
  iv: number
outputs:
  pot: number                  # 0–1
```

---

## Position sizing

### `compute_position_size`
Number of contracts to enter given the user's account size and
risk-per-trade rule.
```
inputs:
  account_size: number
  risk_per_trade_pct: number   # e.g., 0.02 for 2%
  max_loss_per_contract: number  # from compute_max_profit_loss
outputs:
  contracts: integer           # floored to whole contracts
  dollar_risk: number          # actual dollar risk at this count
  pct_of_account: number       # actual pct (may be below the cap)
```

---

## Strategy-rule adherence

### `check_strategy_against_rules`
Evaluate a candidate trade against the user's stated strategy
rules. Returns per-rule pass/fail with the value seen.
```
inputs:
  trade: {legs, ticker, ...}
  rules: {
    iv_rank_min: number | null,
    delta_target: number | null,
    dte_min: number | null,
    dte_max: number | null,
    defined_risk_required: boolean,
    profit_target_pct: number | null,
    stop_loss_pct: number | null,
    universe_filter: object | null,
    ...
  }
  market_state: {iv_rank, current_iv, days_to_expiration, ...}
outputs:
  overall_status: enum["adherent", "non-adherent", "needs-data"]
  rule_results: array[
    {rule_name, status: "pass" | "fail" | "n/a", value_seen, rule_value, note}
  ]
```

This is the function powering "your rule said X; this trade is Y;
mismatch" — the core adherence-coaching feature.

---

## Backtesting

### `run_strategy_backtest`
Run the user's strategy across historical data. Returns aggregate
results with the mandatory hypothetical-performance caveat applied.
```
inputs:
  rules: (same as check_strategy_against_rules)
  start_date: date
  end_date: date
  universe: array[ticker] | "user_universe"
  commission_per_contract: number = 0.65
  fill_assumption: enum["worst_of_bid_ask", "mid"] = "worst_of_bid_ask"
outputs:
  total_trades: integer
  win_rate: number
  avg_win: number
  avg_loss: number
  max_drawdown: number
  sharpe: number               # informational
  trades: array[{entry_date, exit_date, ticker, legs, pnl, exit_reason}]
  disclaimer: string           # mandatory hypothetical-performance text
```

**Output handling**: any UI surface that displays backtest output
MUST render the `disclaimer` field prominently (see
`legal/persistent-disclaimers.md D-6`).

---

## Journal / adherence on real trades

### `score_journal_adherence`
Score the user's real-trade journal against their stated rules.
```
inputs:
  journal: array[
    {date, ticker, legs, entry_price, exit_price, exit_reason, notes}
  ]
  rules: (same as check_strategy_against_rules)
outputs:
  total_trades: integer
  adherent_count: integer
  non_adherent_count: integer
  per_trade: array[
    {trade_id, status: "adherent" | "non-adherent", failed_rules: [...]}
  ]
  patterns: array[
    {pattern_name, description, example_trades}
  ]
  # e.g., "exits losers earlier than stated rule",
  # "increases size after losses", "more revenge trades on losing days"
```

The `patterns` output powers the behavioral-coaching feature
("you tend to exit losers early, sooner than your rule says").

---

## Tools the LLM does NOT have

Explicit non-list to enforce the contract:

- No "recommend_strategy" function.
- No "predict_price" function.
- No "best_trade_today" function.
- No "score_trade_quality" function.
- No "should_user_take_trade" function.
- No tool that reads the user's brokerage holdings directly (the
  journal aggregation feeds the journal/adherence tools, not the
  coach's perception layer).

If a feature request would require any of these, that's the signal
that the request is outside the contract and a redesign is needed.

---

## Engineering notes

- **Tool registration**: register all tools with the LLM via the
  function-calling / tool-use API of the chosen model.
- **Latency budget**: each tool call adds latency. Cache aggressively
  for market data (delayed feed = cache OK for ~5 min). Compute
  tools (pricing, Greeks, P&L) are fast (<10ms) and don't need
  caching.
- **Error handling**: if a tool fails, the LLM should acknowledge
  the failure in voice and pivot ("the data feed is taking a moment
  — while we wait, let's talk through the framework"). Don't
  hallucinate substitute numbers.
- **Determinism**: all math tools should be deterministic given the
  same inputs. Required for evaluation reproducibility.
- **Provider**: under bootstrap, the math layer can be implemented
  in Python (scipy / py_vollib for Greeks, custom for adherence)
  and exposed as REST endpoints or MCP servers. Data layer per
  `compliance/decisions/2026-05-20_compliance-arch.md F`: IEX /
  Polygon delayed / Tradier delayed / Schwab developer API.

## Versioning
Current version: **DRAFT 0.1 — 2026-05-20.** Bump on any
signature addition or change.
