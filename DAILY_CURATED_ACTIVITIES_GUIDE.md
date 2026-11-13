# 365-Day Blockchain Intelligence & Smart Contract Security
## Complete Daily Execution Guide & Curated Activities
*A Day-by-Day Technical Blueprint for Hand-Coding Mastery Without AI Assistance*

---

## The Daily 60-Minute Execution Protocol

Every single day follows this non-negotiable 60-minute time block:

```
[00:00 - 00:15]  15 MIN  |  Pen & Paper Architecture (Notebook only; no keyboard)
[00:15 - 00:50]  35 MIN  |  Strict Cold Coding (Zero AI; official docs whitelist only)
[00:50 - 01:00]  10 MIN  |  Self-Verification, Testing & Git Commit Push
```

### Protocol Rules:
1. **Zero Inline AI**: Disable GitHub Copilot, Cursor Tab, and inline code completion in your editor during this hour.
2. **Docs-Only Whitelist**: Only official documentation (e.g., `docs.python.org`, `evm.codes`, `book.getfoundry.sh`, `docs.soliditylang.org`) is permitted. No ChatGPT, Claude, or StackOverflow copy-pasting.
3. **Paper Before Screen**: If you cannot sketch the data structure, algorithm flow, or EVM storage slot on paper, you are not ready to type.
4. **Daily Git Commit**: Every session ends with a conventional commit pushed to `blockchain-analyst-from-scratch`.

---

# Quarter 1: Cold-Coding Fluency & Data Foundations (Months 1–3)

---

## Month 1: AI Detox & Python Syntax Fluency (Days 1–30)

### Day 1: Ledger Simulation & Top Holder Leaderboard
* **Target File**: `q1_foundations/month01_python_cold/day01_ledger.py`
* **Official Reference**: [Python Dicts & Types](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
* **Pen & Paper Blueprint (15m)**:
  1. Sketch a list of 5 transaction dictionaries on paper: `tx_hash`, `sender`, `receiver`, `amount`, `status` ("success" or "failed").
  2. Write pseudocode to filter out non-successful transactions.
  3. Diagram a net balance table: initialize sender balance subtracting `amount`, receiver balance adding `amount`.
* **Cold-Coding Steps (35m)**:
  1. Create a mock list with at least 8 transactions (including failed txs, circular sends, multiple transfers for one wallet).
  2. Write `filter_valid_transactions(txs: list[dict[str, Any]]) -> list[dict[str, Any]]` using list comprehension or a loop.
  3. Write `compute_balances(txs: list[dict[str, Any]]) -> dict[str, float]`: iterate, initialize missing keys with `0.0`, update balances.
  4. Write `get_leaderboard(balances: dict[str, float], top_n: int = 3) -> list[tuple[str, float]]`: sort by balance descending using `sorted(..., key=lambda x: x[1], reverse=True)`.
* **Verification & Test (10m)**:
  1. Print the filtered transactions; assert no `"status": "failed"` tx is included.
  2. Assert total sum of balances equals `0.0` (closed loop accounting).
  3. Run: `python day01_ledger.py`
* **Commit**: `feat(day01): simulate crypto transaction ledger and balance leaderboard`

---

### Day 2: Payload Sanitizer & Type Coercion
* **Target File**: `q1_foundations/month01_python_cold/day02_sanitizer.py`
* **Official Reference**: [Python Exceptions](https://docs.python.org/3/tutorial/errors.html)
* **Pen & Paper Blueprint (15m)**:
  1. Draw an untrusted dictionary table with edge cases: missing keys, string amounts (`"12.50"`), invalid floats (`"abc"`), negative amounts (`-50`), zero amount (`0`).
  2. Write out safe extraction logic using `.get()`.
* **Cold-Coding Steps (35m)**:
  1. Define `parse_tx(raw: dict[str, Any]) -> Optional[dict[str, Any]]`.
  2. Safely extract `tx_hash` (str), `sender` (str), `receiver` (str), and `amount`.
  3. Inside a `try/except (ValueError, TypeError)` block, coerce `amount` to `float`.
  4. If amount $\le 0$, return `None`. If any required string field is empty or missing, return `None`.
  5. Return a clean sanitized dictionary with guaranteed types.
* **Verification & Test (10m)**:
  1. Create a test array with 6 malformed payloads and 2 valid payloads.
  2. Pass them through `parse_tx` and assert only 2 valid dictionaries are returned.
  3. Run: `python day02_sanitizer.py`
* **Commit**: `feat(day02): build robust transaction sanitizer with safe coercion`

---

### Day 3: Integer Gas & Denomination Calculator
* **Target File**: `q1_foundations/month01_python_cold/day03_gas_calc.py`
* **Official Reference**: [Python Int Math](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
* **Pen & Paper Blueprint (15m)**:
  1. Write out the conversion multipliers: $1 \text{ ETH} = 10^9 \text{ Gwei} = 10^{18} \text{ Wei}$.
  2. Write out why floats are dangerous in crypto: floating point inaccuracies ($0.1 + 0.2 \ne 0.3$).
  3. Formula: $\text{Gas Fee (Wei)} = \text{gas\_used} \times \text{effective\_gas\_price}$.
* **Cold-Coding Steps (35m)**:
  1. Implement `wei_to_gwei(wei: int) -> int` and `gwei_to_wei(gwei: int) -> int` using integer division `//` and multiplication.
  2. Implement `wei_to_eth_str(wei: int) -> str` that formats full ETH to 18 decimals without floating-point drift.
  3. Implement `calculate_tx_gas_fee(gas_used: int, effective_gas_price_wei: int) -> int`.
  4. Implement `flag_gas_outliers(tx_batch: list[dict[str, int]], threshold_wei: int) -> list[dict[str, int]]`.
* **Verification & Test (10m)**:
  1. Test with $10^{18}$ Wei; assert output string equals `"1.0"`.
  2. Test gas calculation with $21,000$ gas used at $50$ Gwei gas price.
  3. Verify outlier detection flags any fee $> 0.05 \text{ ETH}$.
* **Commit**: `feat(day03): implement integer math gas calculator and outlier detector`

---

### Day 4: Stream Deduplication & Reorg Sorter
* **Target File**: `q1_foundations/month01_python_cold/day04_dedup.py`
* **Official Reference**: [Python Sets & Collections](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)
* **Pen & Paper Blueprint (15m)**:
  1. Draw a stream of transactions containing duplicates (e.g., emitted multiple times due to node reconnects or reorgs).
  2. Design order preservation: sets do not maintain original insertion sequence. Write logic combining a `set` for lookup ($O(1)$) with a clean `list` for sequence.
* **Cold-Coding Steps (35m)**:
  1. Define a function `deduplicate_tx_stream(stream: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[str]]`.
  2. Track seen transaction hashes in a `seen_hashes: set[str] = set()`.
  3. Maintain an ordered `clean_stream: list[dict[str, Any]] = []` and a `dropped_hashes: list[str] = []`.
  4. Iterate through records; if hash in `seen_hashes`, log to `dropped_hashes`; otherwise add to set and clean stream.
* **Verification & Test (10m)**:
  1. Create a stream of 10 transactions with 3 duplicate hashes placed at non-consecutive intervals.
  2. Assert length of clean stream is 7, dropped hashes has 3 entries, and original chronological order is intact.
* **Commit**: `feat(day04): deduplicate transaction stream while preserving chronological order`

---

### Day 5: Raw Semicolon CSV Ledger Parser & Exporter
* **Target File**: `q1_foundations/month01_python_cold/day05_csv_export.py`
* **Official Reference**: [Python CSV Module](https://docs.python.org/3/library/csv.html)
* **Pen & Paper Blueprint (15m)**:
  1. Sketch a raw CSV format separated by semicolons: `timestamp;tx_hash;from_addr;to_addr;value_wei`.
  2. Design normalization logic: EVM addresses have mixed checksum casing (`0xAbC...` vs `0xabc...`). Normalize with `.lower()`.
* **Cold-Coding Steps (35m)**:
  1. Use Python's built-in `csv.reader` (delimiter=`;`) to read a simulated ledger export.
  2. Parse columns, normalize addresses to lowercase, and accumulate total `inflow` and `outflow` per address.
  3. Use `csv.DictWriter` to write a clean summary CSV: `address,total_inflow,total_outflow,net_balance`.
* **Verification & Test (10m)**:
  1. Generate a mock 10-line CSV string using `io.StringIO`.
  2. Run the parser and export functions; inspect generated output to verify address casing and arithmetic.
* **Commit**: `feat(day05): parse semicolon delimited ledger and export address summary CSV`

---

### Day 6: Nested JSON Block Payload Parser & Audit Serializer
* **Target File**: `q1_foundations/month01_python_cold/day06_json_blocks.py`
* **Official Reference**: [Python JSON Module](https://docs.python.org/3/library/json.html)
* **Pen & Paper Blueprint (15m)**:
  1. Sketch a nested JSON block payload: `{"block_number": 19000000, "transactions": [{"hash": "0x1", "traces": [{"to": "0xContractA", "type": "call"}, {"to": "0xContractB", "type": "delegatecall"}]}]}`.
  2. Plan traversal logic to extract every contract touched across top-level and internal traces.
* **Cold-Coding Steps (35m)**:
  1. Load nested block payloads using `json.loads()`.
  2. Write recursive or nested loops extracting all unique contract addresses called.
  3. Aggregate metrics: transaction count, trace count, unique contract recipients.
  4. Format and serialize the audit report using `json.dumps(..., indent=2)`.
* **Verification & Test (10m)**:
  1. Run against sample payload; check that `indent=2` serializes valid JSON and catches internal call recipients.
* **Commit**: `feat(day06): parse nested block payloads and serialize contract audit summary`

---

### Day 7: Weekly Review & Strict Mypy Typing Enforcement
* **Target File**: `q1_foundations/month01_python_cold/day07_weekly_review.py`
* **Official Reference**: [Mypy Typing Specs](https://mypy.readthedocs.io/en/stable/)
* **Pen & Paper Blueprint (15m)**:
  1. Review Days 1–6. List all custom types needed: `TxRecord = dict[str, Union[str, int, float]]`, `Address = str`.
  2. Identify potential type leakages where `Any` was used.
* **Cold-Coding Steps (35m)**:
  1. Combine Days 1–6 logic into a single modular CLI script with clean functions and `if __name__ == "__main__":`.
  2. Replace loose `dict` hints with explicit `TypedDict` or `dict[str, Union[str, int]]`.
  3. Annotate every function argument and return value.
* **Verification & Test (10m)**:
  1. Run in PowerShell: `mypy --strict day07_weekly_review.py`.
  2. Manually fix every warning until `Success: no issues found in 1 source file`.
* **Commit**: `refactor(day07): consolidate week 1 pipeline and enforce strict mypy typing`

---

### Days 8–15: Object-Oriented Ledger, Mempool & Cryptographic Trees

* **Day 8 (`day08_wallet_class.py`)**:
  * *Specification*: Build a `Wallet` dataclass tracking `address`, `nonce`, `balance_wei`, and `tx_history`. Implement `send()` and `receive()`. Create custom exception `InsufficientFundsError(Exception)`.
  * *Verification*: Instantiate wallet with 1 ETH, send 0.5 ETH, assert nonce increments to 1. Attempt to send 2 ETH, catch `InsufficientFundsError`.
  * *Commit*: `feat(day08): implement wallet dataclass with custom overdraft exceptions`

* **Day 9 (`day09_mempool.py`)**:
  * *Specification*: Simulate an Ethereum EIP-1559 mempool priority queue using Python's `heapq`. Order pending transactions by `max_priority_fee_per_gas` descending, and break ties by `nonce` ascending for identical senders.
  * *Verification*: Push 6 transactions in random order into heap. Pop transactions sequentially; assert highest miner tip executes first, and nonces for the same address never execute out-of-order.
  * *Commit*: `feat(day09): simulate mempool priority queue using heapq`

* **Day 10 (`day10_merkle.py`)**:
  * *Specification*: Implement a binary Merkle Root calculator using `hashlib.sha256`. Accept a list of transaction hashes. If the leaf count is odd, duplicate the last leaf. Pair adjacent nodes, hash them, and repeat recursively/iteratively until a single 32-byte root hash remains.
  * *Verification*: Calculate root for 1, 2, 3, and 4 hashes. Hand-verify 2-leaf tree: `sha256(leaf0 + leaf1).hexdigest() == root`.
  * *Commit*: `feat(day10): build binary merkle root generator from scratch`

* **Day 11 (`day11_merkle_proof.py`)**:
  * *Specification*: Extend Day 10. Implement `generate_proof(tx_hashes: list[str], target_index: int) -> list[tuple[str, str]]` returning proof hashes with direction (`left`/`right`). Implement `verify_proof(target_tx: str, proof: list[tuple[str, str]], root: str) -> bool`.
  * *Verification*: Generate proof for index 2 in a 4-leaf tree. Call `verify_proof()`; assert returns `True`. Modify one character of `target_tx`; assert returns `False`.
  * *Commit*: `feat(day11): implement cryptographic merkle proof generation and verification`

* **Day 12 (`day12_hex_bytes.py`)**:
  * *Specification*: Write hex/byte conversion helpers without web3 libraries. Slices a 68-byte ERC-20 `transfer(address,uint256)` calldata hex string (`0xa9059cbb...`) into its 4-byte selector, 32-byte padded address, and 32-byte `uint256` token amount converted to integer.
  * *Verification*: Slice known transfer calldata; assert selector is `0xa9059cbb`, extracted address is valid 40-character hex, and value decodes to exact integer.
  * *Commit*: `feat(day12): build calldata slicer for erc20 transfer method`

* **Day 13 (`day13_decorators.py`)**:
  * *Specification*: Hand-code `@retry(max_attempts=3, delay=1.0)` and `@measure_time` decorators using `functools.wraps`. Simulate intermittent RPC failures (`ConnectionResetError`) to demonstrate automatic retry backoff.
  * *Verification*: Decorate a simulated flaky RPC call that fails twice before succeeding; assert function recovers without crashing and prints measured latency.
  * *Commit*: `feat(day13): create custom retry and timing decorators for rpc queries`

* **Day 14 (`day14_mini_chain.py`)**:
  * *Specification*: Build an in-memory 3-block blockchain. Each `Block` holds `index`, `timestamp`, `transactions`, `previous_hash`, and computes its own `current_hash`. Write `is_chain_valid(chain: list[Block]) -> bool`.
  * *Verification*: Verify pristine chain returns `True`. Mutate a transaction in Block 1; verify `is_chain_valid` flags tampering at Block 2.
  * *Commit*: `feat(day14): build in-memory mini blockchain with tamper verification`

* **Day 15 (`day15_generators.py`)**:
  * *Specification*: Write a memory-efficient Python generator function using `yield` that streams simulated transaction logs one line at a time. Filter for swap events with volume $> \$10,000$ without reading the entire dataset into RAM.
  * *Verification*: Stream 100,000 simulated records; monitor memory usage and assert generator yields only high-value events.
  * *Commit*: `feat(day15): stream large transaction logs with memory-efficient generators`

---

### Days 16–23: AMM Math, CLI Tools & Graph Algorithms

* **Day 16 (`day16_amm_math.py`)**:
  * *Specification*: Implement Uniswap V2 constant-product AMM formula: $(x + \Delta x \cdot 0.997)(y - \Delta y) = x \cdot y$. Write `get_amount_out(amount_in: int, reserve_in: int, reserve_out: int, fee_bps: int = 30) -> int` using integer math. Compute price impact percentage.
  * *Verification*: Test pool with $1,000 \text{ ETH}$ and $2,000,000 \text{ USDC}$. Swap $10 \text{ ETH}$; assert returned USDC matches manual calculation.
  * *Commit*: `feat(day16): implement constant product amm swap math with fees`

* **Day 17 (`day17_slippage.py`)**:
  * *Specification*: Extend Day 16. Simulate a series of 20 consecutive swaps against a liquidity pool. Implement `min_amount_out` slippage protection. If price impact causes output to drop below user threshold, raise `SlippageExceededError`. Update reserves after every successful swap.
  * *Verification*: Assert pool price shifts upward after sequential buys. Verify that swap 15 reverts when setting an aggressive slippage tolerance of $0.1\%$.
  * *Commit*: `feat(day17): simulate sequential amm pool swaps with slippage limits`

* **Day 18 (`day18_cli_args.py`)**:
  * *Specification*: Use Python's built-in `argparse` to create a CLI tool accepting `--input <file.json>`, `--min-value <float>`, and `--address <hex>`. Filter transaction JSON and output terminal summary.
  * *Verification*: Run from terminal: `python day18_cli_args.py --input sample.json --min-value 5.0`; verify flags filter correctly.
  * *Commit*: `feat(day18): build command line transaction filter using argparse`

* **Day 19 (`day19_logging.py`)**:
  * *Specification*: Set up Python `logging` module (ban `print()`). Configure both a console `StreamHandler` (INFO level) and a `RotatingFileHandler` (`audit.log`, DEBUG level, 1MB max, 3 backups) with ISO timestamps and log levels.
  * *Verification*: Trigger transactions; assert terminal displays clean summaries while `audit.log` records detailed execution traces.
  * *Commit*: `feat(day19): configure structured rotating file and console logging`

* **Day 20 (`day20_context_mgr.py`)**:
  * *Specification*: Build a custom context manager class (`AtomicLedgerWriter`) using `__enter__` and `__exit__`. Write ledger state to a temporary file (`.tmp`), and rename to final destination file only if no exception occurred during the block.
  * *Verification*: Trigger a mid-write exception; verify temporary file is purged and original ledger file remains uncorrupted.
  * *Commit*: `feat(day20): build atomic ledger snapshot context manager`

* **Day 21 (`day21_graph_adj.py`)**:
  * *Specification*: Represent wallet fund flows as a directed weighted graph using `collections.defaultdict(lambda: collections.defaultdict(float))`. Write functions to compute in-degree, out-degree, and highest-volume counterparty per wallet.
  * *Verification*: Load 10 transfers; assert target exchange wallet has in-degree of 4 and out-degree of 0.
  * *Commit*: `feat(day21): model transaction fund flows as directed weighted graph`

* **Day 22 (`day22_bfs_trace.py`)**:
  * *Specification*: Implement Breadth-First Search (BFS) using `collections.deque` on the fund flow graph. Find the shortest hop path between a flagged hacker wallet and a centralized exchange deposit address.
  * *Verification*: Run BFS across a 5-tier multi-hop transfer tree; assert it returns the exact sequence of intermediate wallets: `[Hacker -> Hop1 -> Hop2 -> Exchange]`.
  * *Commit*: `feat(day22): implement bfs shortest path search for fund flow tracing`

* **Day 23 (`day23_dfs_cycles.py`)**:
  * *Specification*: Implement Depth-First Search (DFS) with a recursion stack to detect circular wash-trading loops ($A \to B \to C \to A$) within a set of transaction records.
  * *Verification*: Inject a 3-party wash-trade loop into a graph of 50 normal transactions; assert DFS detects and outputs the exact cyclic loop addresses.
  * *Commit*: `feat(day23): detect circular wash trading loops with dfs cycle detection`

---

### Days 24–30: Production Utilities & Month 1 Capstone

* **Day 24 (`day24_http_client.py`)**:
  * *Specification*: Using `urllib.request` or `requests`, query a public crypto API (e.g., CoinGecko simple price or DefiLlama). Implement backoff on HTTP 429 rate limits, socket timeouts, and in-memory TTL caching (60s).
  * *Verification*: Make 5 rapid calls for ETH price; assert only the first call hits the network and remaining 4 return cached results.
  * *Commit*: `feat(day24): build rate-limit resilient http price client with ttl cache`

* **Day 25 (`day25_env_config.py`)**:
  * *Specification*: Build a strict configuration loader reading environment variables via `os.environ`. Validate presence of `RPC_URL` (must start with `http://` or `wss://`) and numerical thresholds (`MIN_WHALE_USD`). Fail fast at startup with descriptive error if missing.
  * *Verification*: Test with missing variable; assert program raises `ConfigurationError` and exits immediately.
  * *Commit*: `feat(day25): implement fail-fast environment configuration validator`

* **Day 26 (`day26_regex_parse.py`)**:
  * *Specification*: Write regular expressions using `re` to extract all 42-character EVM addresses (`0x[a-fA-F0-9]{40}`) and 66-character tx hashes (`0x[a-fA-F0-9]{64}`) from messy incident reports or chat logs.
  * *Verification*: Pass a mock incident chat dump containing markdown, URLs, and addresses; assert all unique addresses and hashes are extracted cleanly.
  * *Commit*: `feat(day26): extract evm addresses and tx hashes with regex`

* **Day 27 (`day27_twap.py`)**:
  * *Specification*: Implement a Time-Weighted Average Price (TWAP) calculation engine. Given an array of `(timestamp, price)` tuples with non-uniform time intervals, calculate the exact TWAP across a user-defined window: $\frac{\sum P_i \cdot \Delta t_i}{\sum \Delta t_i}$.
  * *Verification*: Test with 3 checkpoints: 100 USD for 10s, 200 USD for 30s; assert TWAP equals 175 USD.
  * *Commit*: `feat(day27): build time weighted average price calculator`

* **Day 28 (`day28_reconcile.py`)**:
  * *Specification*: Build an internal ledger reconciliation engine. Compare an internal accounting database export against an on-chain ledger export. Output discrepancies: missing transaction hashes, mismatched statuses, and balance deltas per address.
  * *Verification*: Pass two datasets with 2 intentional mismatches; verify output report highlights exact differing transaction records.
  * *Commit*: `feat(day28): implement ledger reconciliation and discrepancy reporter`

* **Day 29 (`day29_refactor/`)**:
  * *Specification*: Refactor all Month 1 utilities into a professional Python package structure: `src/ledger_core/` with `__init__.py`, `sanitizer.py`, `graph.py`, `amm.py`, and `types.py`. Ensure zero circular imports and 100% `mypy --strict` compliance.
  * *Verification*: Run `mypy --strict src/ledger_core`; assert zero warnings.
  * *Commit*: `refactor(day29): package month 1 utilities into typed ledger_core module`

* **Day 30 (`day30_capstone_cli.py`)**:
  * *Specification*: **Month 1 Capstone Project**. Build an end-to-end command-line On-Chain Ledger Analyzer. The tool ingests raw JSON blocks, sanitizes payloads, constructs a fund-flow graph, detects wash-trading loops, identifies whale balances, and outputs a structured JSON analysis report.
  * *Verification*: Run CLI tool on a test suite of 500 simulated transactions; verify full report generation without errors.
  * *Tag*: `git tag -a v0.1-month1-capstone -m "Deliverable: Hand-coded CLI On-Chain Ledger Analyzer"`
  * *Commit*: `feat(day30): ship month 1 capstone cli on-chain ledger analyzer`

---

## Month 2: Custom Algorithms, Validation & Async Pipelines (Days 31–60)

### Days 31–35: Algorithmic Foundations
* **Day 31 (`day31_rate_limit.py`)**: Implement a Token-Bucket Rate Limiter from scratch without third-party libraries. Track token replenishment rate and burst capacity for RPC clients.
* **Day 32 (`day32_sliding_window.py`)**: Implement a Sliding-Window Anomaly Detector using a circular buffer to detect volume spikes (sudden $5\times$ deviations over baseline).
* **Day 33 (`day33_binary_search.py`)**: Implement Binary Search to locate an Ethereum block number given a Unix timestamp, assuming block timestamps are monotonically increasing.
* **Day 34 (`day34_lru_cache.py`)**: Build an LRU (Least Recently Used) Cache from scratch using `collections.OrderedDict` with get/put operations running in $O(1)$ time complexity.
* **Day 35 (`day35_orderbook.py`)**: Build a Price-Time Priority Limit Order Book matching engine supporting Buy/Sell limit orders and partial fills.

### Days 36–42: Strict Schema Validation with Pydantic v2
* **Days 36–37 (`day36_schemas.py`)**: Define strictly typed Pydantic models for Ethereum Block headers, Transactions, and Event Logs.
* **Days 38–39 (`day38_validators.py`)**: Write custom `@field_validator` functions checking 42-character `0x` hex prefixes, 32-byte hash lengths, and non-negative gas values.
* **Days 40–41 (`day40_unions.py`)**: Model discriminated union types for Legacy Transactions (Type 0), EIP-2930 (Type 1), and EIP-1559 (Type 2).
* **Day 42 (`day42_dead_letter.py`)**: Build a Dead-Letter Queue (DLQ) pipeline: route malformed JSON payloads to a quarantine file with exact Pydantic validation error traces.

### Days 43–50: Asynchronous Concurrency (`asyncio` & `httpx`)
* **Days 43–44 (`day43_async_basics.py`)**: Write async coroutines utilizing `asyncio.gather()` to fetch multiple wallet balances concurrently without blocking.
* **Days 45–46 (`day45_semaphore.py`)**: Bound concurrent requests using `asyncio.Semaphore(10)` to prevent HTTP 429 rate limits against public RPC nodes.
* **Days 47–48 (`day47_worker_queue.py`)**: Implement an asynchronous producer-consumer pipeline using `asyncio.Queue` separating block ingestion from transaction parsing.
* **Days 49–50 (`day49_balance_crawler.py`)**: Build a high-throughput async balance crawler fetching 500 mock wallet balances concurrently in under 3 seconds.

### Days 51–56: Test-Driven Security Mindset (`pytest`)
* **Days 51–52 (`tests/test_ledger.py`)**: Write parameterized unit tests (`@pytest.mark.parametrize`) testing edge cases: zero transfers, overflow conditions, fee rounding.
* **Days 53–54 (`tests/test_mock_rpc.py`)**: Mock network drops, HTTP 500 errors, and timeout retries using `unittest.mock.AsyncMock`.
* **Days 55–56 (`tests/test_amm_invariants.py`)**: Write invariant property tests: assert total pool constant $k$ never decreases after any swap sequence ($k_{\text{after}} \ge k_{\text{before}}$).

### Days 57–60: Month 2 Capstone
* **Day 57–60 (`day60_async_etl.py`)**: **Month 2 Capstone Project**. Architect a fault-tolerant async ETL pipeline. Ingest block streams asynchronously, validate schemas with Pydantic, filter high-value whale transfers, handle worker failures gracefully, and pass 100% of unit tests and `mypy --strict`.
* *Tag*: `git tag -a v0.2-month2-capstone -m "Deliverable: Fault-Tolerant Async Blockchain ETL Pipeline"`

---

## Month 3: Relational SQL, Dune Analytics & TypeScript Foundations (Days 61–90)

### Days 61–67: PostgreSQL Ledger Modeling
* **Days 61–62 (`day61_schema.sql`)**: Hand-write normalized DDL schemas for `blocks`, `transactions`, and `erc20_transfers`. Use `NUMERIC(78, 0)` for storing exact 256-bit unsigned integers without truncation.
* **Days 63–65 (`day63_ingest.py`)**: Write Python `psycopg` batch insert scripts using `ON CONFLICT (tx_hash) DO NOTHING` for idempotent ingestion.
* **Days 66–67 (`day66_indexes.sql`)**: Profile slow queries using `EXPLAIN ANALYZE`. Design composite B-Tree indexes on `(to_address, block_timestamp)` and `(from_address, block_timestamp)` to optimize transfer lookups.

### Days 68–75: Analytical SQL & Window Functions
* **Days 68–70 (`day68_ctes.sql`)**: Write Common Table Expressions (CTEs) computing Daily Active Wallets (DAU) and protocol inflow vs. outflow.
* **Days 71–73 (`day71_window.sql`)**: Use `LAG()`, `LEAD()`, and rolling 7-day `SUM() OVER (PARTITION BY address ORDER BY block_time)` to detect rapid whale accumulation.
* **Days 74–75 (`day74_retention.sql`)**: Hand-code weekly cohort retention matrices measuring returning DeFi protocol users over 12 weeks.

### Days 76–82: Live On-Chain Analysis on Dune Analytics
* **Days 76–78 (`dune_01_dex.sql`)**: Write queries against decoded Ethereum tables (`dex.trades`, `uniswap_v2_ethereum.Pair_evt_Swap`) to compute 24h volume and fee generation.
* **Days 79–80 (`dune_02_liquidity.sql`)**: Query LP position distributions and identify top 1% liquidity providers controlling pool depth.
* **Days 81–82 (`dune_03_bridge.sql`)**: Build and publish 2 public dashboards tracking cross-chain bridge net flows (Arbitrum / Base bridges). Include live Dune links in your repo.

### Days 83–90: Strict TypeScript Transition
* **Days 83–84 (`tsconfig.json`, `day83_types.ts`)**: Configure TypeScript compiler with `"strict": true`, `"noImplicitAny": true`. Define interfaces for transactions, logs, and receipts.
* **Days 85–87 (`day85_ledger.ts`)**: Rewrite your Day 1 ledger parser and balance aggregator in strict TypeScript using `Map<string, bigint>`.
* **Days 88–90 (`day88_rpc_ts.ts`)**: Hand-code a typed JSON-RPC client in TypeScript using native `fetch()` without ethers/viem libraries.

---

# Quarter 2: On-Chain Mechanics & EVM Internals (Months 4–6)

---

## Month 4: JSON-RPC Internals, ABI Encoding & Event Logs (Days 91–120)

### Days 91–97: Raw JSON-RPC 2.0 Payloads
* **Days 91–93 (`day91_raw_rpc.py`)**: Send raw HTTP POST payloads to Ethereum/Base nodes (`eth_blockNumber`, `eth_getBlockByNumber`). Inspect hex-encoded response fields manually.
* **Days 94–95 (`day94_receipts.py`)**: Query `eth_getTransactionReceipt`. Parse gas used, cumulative gas, effective gas price, and contract creation addresses.
* **Days 96–97 (`day96_bloom.py`)**: Inspect the 256-byte `logsBloom` filter in block headers; write a Python bitwise checker testing if an address or topic is potentially present in a block.

### Days 98–105: ABI Encoding & Calldata Decoding
* **Days 98–100 (`day98_selectors.py`)**: Compute 4-byte function selectors manually by taking `keccak256("functionName(type1,type2)")[:4]`. Build a reverse-lookup dictionary of common DeFi selectors.
* **Days 101–105 (`day101_calldata.py`)**: Hand-decode ABI calldata containing dynamic types (`string`, `bytes`, `uint256[]`). Decode offset pointers and lengths step-by-step.

### Days 106–113: Event Log Filtering & Multicall3 Batching
* **Days 106–109 (`day106_logs.py`)**: Query `eth_getLogs` using indexed topics (`topics[0]` = event signature hash). Build pagination logic handling RPC 10,000-log maximum response limits.
* **Days 110–113 (`day110_multicall.py`)**: Construct a single batch call to `Multicall3.aggregate3` to query balances of 100 token contracts in a single round-trip RPC request.

### Days 114–120: Month 4 Capstone
* **Days 114–120 (`day120_tx_decoder.py`)**: **Month 4 Capstone Project**. Build a CLI Transaction Decoder. Accepts any Ethereum tx hash, fetches transaction & receipt, decodes calldata, decodes all emitted ERC-20 / Uniswap swap logs, and prints an execution breakdown.
* *Tag*: `git tag -a v0.4-month4-capstone -m "Deliverable: CLI Ethereum Transaction & Log Decoder"`

---

## Month 5: Real-Time Blockchain Indexing & Reorg Handling (Days 121–150)

### Days 121–128: Fault-Tolerant Block Cursor & Reorg Engine
* **Days 121–124 (`day121_cursor.py`)**: Build a persistent block ingestion cursor stored in PostgreSQL. On each new block, assert `block.parentHash == last_indexed_block.hash`.
* **Days 125–128 (`day125_reorg.py`)**: Write an automated chain reorganization rollback handler. When a parent hash mismatch occurs, step back block-by-block to find the common ancestor, delete orphaned records, and re-index the canonical chain.

### Days 129–136: WebSocket Streaming & DEX State Sync
* **Days 129–132 (`day129_ws_sub.py`)**: Subscribe to `newHeads` and `logs` via WebSockets. Implement heartbeat pings and exponential-backoff automatic reconnection.
* **Days 133–136 (`day133_dex_sync.py`)**: Stream Uniswap V2 `Sync` and Uniswap V3 `Swap` events in real-time. Compute real-time pool prices and detect large trades ($> \$50,000$).

### Days 137–150: Milestone 1 Project — Real-Time Alert Indexer
* **Days 137–150 (`indexer_project/`)**: **Milestone Project 1**. Hand-code a production-grade Real-Time Whale & DEX Liquidity Alert Indexer. Backed by PostgreSQL, Docker Compose setup, reorg-safe block cursor, WebSocket log listener, Discord/Telegram webhook alert integration, and comprehensive README documentation.
* *Tag*: `git tag -a v0.5-milestone-indexer -m "Milestone 1: Production Real-Time Whale & DEX Alert Indexer"`

---

## Month 6: Solidity Engineering & EVM Bytecode Internals (Days 151–180)

### Days 151–158: Hand-Writing Core Solidity Contracts
* **Days 151–152 (`Day151_Token.sol`)**: Write an ERC-20 token from scratch without importing OpenZeppelin. Implement `transfer`, `approve`, and `transferFrom`.
* **Days 153–154 (`Day153_Vault.sol`)**: Build an ETH vault contract with deposit, withdrawal, and accounting logic using custom errors (`error InsufficientBalance()`).
* **Days 155–156 (`Day155_Access.sol`)**: Implement Role-Based Access Control (RBAC) with owner transfer and multi-role modifiers (`onlyRole`).
* **Days 157–158 (`Day157_Escrow.sol`)**: Hand-code a time-locked two-party escrow contract with timeout dispute resolution.

### Days 159–166: EVM Storage Layout & Slot Arithmetic
* **Days 159–161 (`Day159_Slots.sol`)**: Map 32-byte storage slots on paper. Pack variables into single 32-byte slots (`uint128`, `uint64`, `address`).
* **Days 162–164 (`Day162_Mappings.sol`)**: Calculate exact storage slots for mappings and dynamic arrays: $\text{slot} = \text{keccak256}(\text{abi.encode}(key, \text{slot\_index}))$. Verify via `cast storage` or `eth_getStorageAt`.
* **Days 165–166 (`Day165_Collisions.sol`)**: Demonstrate how misaligned storage layouts between proxy and implementation contracts result in critical storage collision.

### Days 167–174: EVM Opcodes, Stack & Memory
* **Days 167–170 (`day167_opcodes.md`)**: Step through raw EVM opcodes using `evm.codes`: stack manipulation (`PUSH`, `POP`, `DUP`, `SWAP`), arithmetic (`ADD`, `MUL`), memory (`MLOAD`, `MSTORE`), and storage (`SLOAD`, `SSTORE`).
* **Days 171–174 (`Day171_Proxy.sol`)**: Hand-code a minimal EIP-1967 ERC-1967 proxy using Yul assembly `delegatecall`. Explain why execution runs in the context of the caller.

### Days 175–180: Month 6 Capstone
* **Days 175–180 (`day180_disasm.py`)**: **Month 6 Capstone Project**. Write a Python EVM Bytecode Disassembler. Fetches runtime bytecode via `eth_getCode`, parses raw hex into opcodes, extracts embedded 4-byte function selectors, and flags dangerous opcodes (`DELEGATECALL`, `SELFDESTRUCT`).
* *Tag*: `git tag -a v0.6-month6-capstone -m "Deliverable: Hand-Coded EVM Bytecode Disassembler"`

---

# Quarter 3: Smart Contract Security & Vulnerability Analysis (Months 7–9)

---

## Month 7: Foundry Testing, Mainnet Forking & Static Analysis (Days 181–210)

### Days 181–188: Foundry CLI & Unit Testing
* **Days 181–184 (`day181_cast.sh`)**: Master the `cast` CLI: inspect storage slots (`cast storage`), compute signatures (`cast sig`), decode calldata (`cast 4byte-decode`), and simulate RPC calls (`cast call`).
* **Days 185–188 (`test/Vault.t.sol`)**: Write Foundry unit tests. Master cheatcodes: `vm.prank(alice)` (caller impersonation), `vm.deal(alice, 10 ether)` (ETH funding), `vm.warp(block.timestamp + 1 days)` (time travel), and `vm.expectRevert()`.

### Days 189–196: Stateless Fuzzing & Stateful Invariants
* **Days 189–192 (`test/VaultFuzz.t.sol`)**: Write property-based fuzz tests. Use `vm.assume()` and `bound()` to fuzz deposit amounts across edge cases without overflow.
* **Days 193–196 (`test/VaultInvariant.t.sol`)**: Hand-code stateful invariant tests. Define handler contracts and assert core protocol invariants: $\text{address}(vault).\text{balance} \ge \text{totalDeposits}$ across 10,000 random multi-actor call sequences.

### Days 197–204: Slither Static Analysis & Custom Detectors
* **Days 197–200 (`slither_triage.md`)**: Run Slither against 5 open-source protocol repositories. Triage findings, separating true positives from false alarms.
* **Days 201–204 (`custom_detector.py`)**: Write a custom Slither detector in Python. Traverse the contract AST (Abstract Syntax Tree) to flag state-modifying functions missing access control modifiers.

### Days 205–210: Month 7 Capstone
* **Days 205–210 (`test/MainnetFork.t.sol`)**: **Month 7 Capstone Project**. Fork Ethereum mainnet at a specific block height in Foundry (`vm.createSelectFork`). Impersonate a whale address, execute a multi-hop swap on Uniswap V3, deposit collateral into Aave V3, borrow USDC, and assert precise balance updates.
* *Tag*: `git tag -a v0.7-month7-capstone -m "Deliverable: Mainnet Fork DeFi Simulation in Foundry"`

---

## Month 8: Smart Contract Vulnerability Mechanics & Wargames (Days 211–240)

### Days 211–218: Reentrancy Exploits
* **Days 211–213 (`test/SingleReentrancy.t.sol`)**: Write a vulnerable vault and an attacker contract exploiting classic single-function reentrancy. Implement Checks-Effects-Interactions (CEI) and `ReentrancyGuard` to verify fix.
* **Days 214–216 (`test/CrossFunctionReentrancy.t.sol`)**: Code and exploit a cross-function reentrancy vulnerability where one function updates balance while another allows transfer before balance update.
* **Days 217–218 (`test/ReadOnlyReentrancy.t.sol`)**: Reproduce a read-only reentrancy attack: manipulate an AMM curve mid-removal to feed a distorted spot-price to a third-party lending protocol.

### Days 219–226: Arithmetic, Precision Loss & Vault Inflation
* **Days 219–222 (`test/PrecisionLoss.t.sol`)**: Exploit integer division before multiplication ($a / b \times c$ vs $a \times c / b$). Demonstrate how rounding down to zero allows free fee-less actions.
* **Days 223–226 (`test/VaultInflation.t.sol`)**: Hand-code an ERC-4626 first-depositor inflation attack. Donate underlying assets directly to the vault to inflate share prices, causing subsequent user deposits to round to 0 shares.

### Days 227–233: Signatures, Access Control & Oracle Manipulation
* **Days 227–229 (`test/SigReplay.t.sol`)**: Exploit signature replay: execute identical signatures across multiple transactions due to missing nonces or missing `chainId` domain separators.
* **Days 230–233 (`test/OracleManipulation.t.sol`)**: Build a flash-loan oracle manipulation exploit. Borrow $10,000,000$ in a flash loan, skew a Uniswap V2 reserve pool, trigger an under-collateralized loan on a lending protocol, and repay the flash loan with profit.

### Days 234–240: Wargame Gauntlet
* **Days 234–240 (`wargames/`)**: Solve 10+ levels of Ethernaut and Damn Vulnerable DeFi (e.g., Unstoppable, Naive Receiver, Truster, Side Entrance, Puppet). Hand-write every attacker contract and Foundry test from scratch without looking at solutions.
* *Tag*: `git tag -a v0.8-month8-wargames -m "Deliverable: Hand-Coded Wargame Exploit Suite"`

---

## Month 9: Historical DeFi Hack Reproduction & Root-Cause Post-Mortems (Days 241–270)

### Days 241–248: Execution Call-Trace Forensics
* **Days 241–244 (`traces/trace_analysis_01.md`)**: Inspect historical hack transactions on Phalcon / Tenderly. Diagram the complete call tree on paper (Caller $\to$ FlashLoan $\to$ VulnerableContract $\to$ Drain).
* **Days 245–248 (`traces/trace_analysis_02.md`)**: Identify the exact line of Solidity code where state was corrupted or invariant broken for 4 major hacks.

### Days 249–262: Standalone Foundry Fork Exploit Reproductions
* **Days 249–253 (`test/Hack1_FlashLoanOracle.t.sol`)**: Fork mainnet 1 block prior to a major historical flash-loan oracle exploit (e.g., bZx or Cream Finance). Write a standalone exploit contract reproducing the drain in a single transaction.
* **Days 254–258 (`test/Hack2_Reentrancy.t.sol`)**: Reproduce a multi-million-dollar reentrancy hack (e.g., Grim Finance or DFX Finance).
* **Days 259–262 (`test/Hack3_LogicError.t.sol`)**: Reproduce an access-control or validation bypass exploit (e.g., Nomad Bridge or Wormhole).

### Days 263–270: Milestone 2 Project — Defi Post-Mortem Repository
* **Days 263–270 (`defi_postmortems/`)**: **Milestone Project 2**. Publish a GitHub showcase repository containing your 3 reproducible Foundry exploit tests, complete with formal written root-cause analysis reports, step-by-step transaction breakdowns, and exact patched code diffs.
* *Tag*: `git tag -a v0.9-milestone-postmortems -m "Milestone 2: 3 Historical Hack Reproductions with Root-Cause Writeups"`

---

# Quarter 4: Public Proof-of-Work & Job Hunting (Months 10–12)

---

## Month 10: On-Chain Threat Intelligence & Fund-Flow Forensics (Days 271–300)

### Days 271–278: Entity Clustering Heuristics
* **Days 271–274 (`day271_clustering.py`)**: Implement Python heuristics linking disparate addresses based on shared initial gas funding sources (deposit address reuse).
* **Days 275–278 (`day275_correlation.py`)**: Write timing and nonce correlation algorithms to identify clusters of wallets operating synchronously under automated bot control.

### Days 279–288: Cross-Chain & Privacy Mixer Tracing
* **Days 279–283 (`day279_bridge_tracer.py`)**: Trace stolen fund movement across cross-chain bridges (Stargate, Across, Synapse) by matching deposit events on the source chain with release events on the destination chain.
* **Days 284–288 (`day284_flow_graph.py`)**: Write a Python tool that exports on-chain multi-hop fund flows into structured JSON and Graphviz / Mermaid visualization diagrams.

### Days 289–300: Month 10 Capstone
* **Days 289–300 (`investigation_01.md`)**: **Month 10 Capstone Project**. Conduct an end-to-end forensic investigation of a recent on-chain exploit or rug pull. Document initial funding wallet, attacker contract deployment, execution transactions, bridge laundering paths, and current holding addresses in a formal intelligence brief.
* *Tag*: `git tag -a v0.10-month10-forensics -m "Deliverable: Formal On-Chain Forensic Investigation Report"`

---

## Month 11: Live Competitive Audits & Protocol Threat Modeling (Days 301–330)

### Days 301–314: Competitive Audit Contest #1
* **Days 301–304**: Enter a live competitive audit contest on Sherlock, Cantina, or Code4rena. Map protocol architecture, actor permissions, and trust boundaries on paper.
* **Days 305–310**: Audit high-risk state transitions manually: collateral valuation, liquidations, reward distributions, deposit/withdrawal accounting.
* **Days 311–314 (`contest_01/`)**: Write clean, reproducible Foundry PoCs for discovered Medium/High vulnerabilities. Submit formal reports adhering to contest submission guidelines.

### Days 315–324: Competitive Audit Contest #2
* **Days 315–324 (`contest_02/`)**: Enter a second live audit contest on a different protocol architecture (e.g., staking, DEX, or restaking). Execute the complete audit methodology under live deadline pressure.

### Days 325–330: Retrospective Gap Analysis
* **Days 325–330 (`audit_retrospective.md`)**: Review official judging results and winning warden submissions. For every vulnerability you missed:
  1. Write a Foundry PoC reproducing the missed bug.
  2. Document the root reason you overlooked it (e.g., assumed function was private, missed precision rounding).
  3. Add the bug pattern to your personal auditing checklist.

---

## Month 12: Portfolio Consolidation & Targeted Hiring Execution (Days 331–365)

### Days 331–342: Flagship Deliverable Showcase Packaging
* **Days 331–336 (`portfolio_hub/README.md`)**: Curate your top 5 deliverables into a clean showcase:
  1. Real-Time Alert Indexer (Milestone 1)
  2. 2 Live Dune Analytics Dashboards
  3. 3 Historical Hack Reproductions & Postmortems (Milestone 2)
  4. On-Chain Forensic Investigation Brief
  5. Competitive Audit Contest Findings & Retrospective
* **Days 337–342**: Polish documentation, add architectural flowcharts, and ensure every test passes with `forge test` and `pytest`.

### Days 343–352: Positioning & Direct Hiring Outreach
* **Days 343–346 (`resume_and_outreach.md`)**: Update your resume and LinkedIn. Highlight your Computer Science / Software Engineering degree, hands-on EVM internals knowledge, and the verifiable 365-day hand-coded GitHub commit history.
* **Days 347–352**: Direct outreach to security leads, audit firm founders, and analytics managers at 25 target firms (Chainalysis, TRM Labs, OpenZeppelin, Trail of Bits, Spearbit). Include direct links to your specific hack reproductions and forensic reports.

### Days 353–365: Live Technical Interview Gauntlet
* **Days 353–358 (`interview_drills/`)**: Practice timed 45-minute cold-coding drills: integer gas math, Merkle tree generation, reentrancy exploit contracts, and SQL window functions.
* **Days 359–365**: Practice live smart contract walkthroughs out loud: explain EVM storage layouts, opcode gas costs, and call trace logs until you can articulate complex blockchain concepts effortlessly.
* *Tag*: `git tag -a v1.0-graduate -m "365-Day Program Completed: Autonomous Web3 Security Auditor & Intelligence Analyst"`

---

## Master Verification & Quality Checklist

Before committing any day's work, confirm:
- [ ] Logic was drafted on paper first during the first 15 minutes.
- [ ] No inline AI autocomplete or LLM chat was used to write the code.
- [ ] Only official documentation was referenced.
- [ ] Code passes verification tests without errors (`python`, `mypy --strict`, or `forge test`).
- [ ] Commit uses Conventional Commits (`feat:`, `test:`, `exploit:`, `docs:`).
- [ ] Commit is pushed to remote `origin main`.

