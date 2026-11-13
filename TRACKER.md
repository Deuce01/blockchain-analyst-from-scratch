# 365-Day Blockchain Intelligence & Smart Contract Security Tracker

*Author*: [deuce01](https://github.com/deuce01) | *Email*: chegev704@gmail.com  
*Status*: Active (Days 1–365)

---

## 📊 Overall Progress Summary

- [ ] **Quarter 1**: Cold-Coding Fluency & Data Foundations (Days 1–90)
- [ ] **Quarter 2**: On-Chain Mechanics & EVM Internals (Days 91–150)
- [ ] **Quarter 3**: Smart Contract Security & Exploits (Days 151–270)
- [ ] **Quarter 4**: Forensics, Audits & Portfolio (Days 271–365)

---

## Quarter 1: Cold-Coding Fluency & Data Foundations (Days 1–90)

### Month 1: AI Detox & Python Syntax Fluency (Days 1–30)
- [ ] **Day 01**: `day01_ledger.py` — Filter status & calculate balance leaderboard
- [ ] **Day 02**: `day02_sanitizer.py` — Safe parsing with `.get()`, float coercion & None checks
- [ ] **Day 03**: `day03_gas_calc.py` — Integer Wei/Gwei/ETH conversion & gas fee calculations
- [ ] **Day 04**: `day04_dedup.py` — Chronological set deduplication of reorged transactions
- [ ] **Day 05**: `day05_csv_export.py` — Semicolon ledger parse & normalized address summary export
- [ ] **Day 06**: `day06_json_blocks.py` — Block JSON parse, unique contract interactions & audit report
- [ ] **Day 07**: `day07_weekly_review.py` — Unified modular script passing `mypy --strict`
- [ ] **Day 08**: `day08_wallet_class.py` — Wallet dataclass with custom `InsufficientFundsError`
- [ ] **Day 09**: `day09_mempool.py` — Mempool priority queue using `heapq` (gas & nonce ordering)
- [ ] **Day 10**: `day10_merkle.py` — Binary Merkle Root generator using `hashlib.sha256`
- [ ] **Day 11**: `day11_merkle_proof.py` — Merkle proof generation & verification functions
- [ ] **Day 12**: `day12_hex_bytes.py` — Calldata slicing for 4-byte selector & 32-byte parameters
- [ ] **Day 13**: `day13_decorators.py` — Custom `@retry` and `@measure_time` decorators
- [ ] **Day 14**: `day14_mini_chain.py` — In-memory 3-block linked chain with tamper detection
- [ ] **Day 15**: `day15_generators.py` — Memory-efficient log streaming generator
- [ ] **Day 16**: `day16_amm_math.py` — Constant-product AMM simulator (`x * y = k`)
- [ ] **Day 17**: `day17_slippage.py` — Swap sequence with `min_amount_out` slippage protection
- [ ] **Day 18**: `day18_cli_args.py` — CLI transaction filter using `argparse`
- [ ] **Day 19**: `day19_logging.py` — Production structured logging (console + rotating file)
- [ ] **Day 20**: `day20_context_mgr.py` — Atomic file lock context manager (`__enter__` / `__exit__`)
- [ ] **Day 21**: `day21_graph_adj.py` — Directed weighted transaction graph representation
- [ ] **Day 22**: `day22_bfs_trace.py` — BFS shortest hop path from hacker address to exchange
- [ ] **Day 23**: `day23_dfs_cycles.py` — DFS recursion-stack circular wash trade detection
- [ ] **Day 24**: `day24_http_client.py` — HTTP client with rate-limit handling & TTL cache
- [ ] **Day 25**: `day25_env_config.py` — Strict environment configuration validator
- [ ] **Day 26**: `day26_regex_parse.py` — Regex parser for EVM addresses & transaction hashes
- [ ] **Day 27**: `day27_twap.py` — Time-weighted average price (TWAP) calculator
- [ ] **Day 28**: `day28_reconcile.py` — Reconciliation engine comparing DB vs on-chain ledger
- [ ] **Day 29**: `day29_refactor/` — Package refactoring (`src/ledger_core`) with strict typing
- [ ] **Day 30**: `day30_capstone_cli.py` — **Capstone: CLI On-Chain Ledger Analyzer**

### Month 2: Custom Algorithms, Validation & Async Pipelines (Days 31–60)
- [ ] **Days 31–35**: Algorithmic Foundations (Token-bucket rate limiter, sliding window, LRU, Orderbook)
- [ ] **Days 36–42**: Strict Pydantic v2 Models & Schema Validation (Block, Tx, Log models, Dead-letter queue)
- [ ] **Days 43–50**: Asynchronous Concurrency (`asyncio`, `httpx`, bounded Semaphores, Worker queues)
- [ ] **Days 51–56**: Test-Driven Security Mindset (`pytest`, mocks, invariant properties)
- [ ] **Days 57–60**: `day60_async_etl.py` — **Capstone: Fault-Tolerant Async ETL Pipeline**

### Month 3: Relational SQL, Dune Analytics & TypeScript Foundations (Days 61–90)
- [ ] **Days 61–67**: PostgreSQL Ledger Modeling (`NUMERIC(78, 0)`, psycopg batch inserts, B-tree indexes)
- [ ] **Days 68–75**: Analytical SQL, CTEs & Window Functions (`LAG`, `LEAD`, rolling 7-day accumulation)
- [ ] **Days 76–82**: Live Dune Analytics Queries & 2 Public Dashboards
- [ ] **Days 83–90**: Strict TypeScript Transition (`tsconfig.json`, interfaces, typed RPC fetch)

---

## Quarter 2: On-Chain Mechanics & EVM Internals (Days 91–180)

### Month 4: JSON-RPC Internals, ABI Encoding & Event Logs (Days 91–120)
- [ ] **Days 91–97**: Raw JSON-RPC 2.0 payloads via HTTP POST (`eth_blockNumber`, receipts, bloom filters)
- [ ] **Days 98–105**: 4-Byte Function Selectors & Calldata Offset Decoding (`eth_abi`)
- [ ] **Days 106–113**: Event Log Filtering (`topics[0..3]`) & Multicall3 Batching
- [ ] **Days 114–120**: `day120_tx_decoder.py` — **Capstone: Command-Line Transaction Decoder**

### Month 5: Real-Time Blockchain Indexing & Reorg Handling (Days 121–150)
- [ ] **Days 121–128**: Persistent Block Cursor & Chain Reorganization Rollback Engine
- [ ] **Days 129–136**: WebSocket Streaming (`newHeads`, Uniswap V2/V3 sync & swap decoding)
- [ ] **Days 137–150**: `indexer_project/` — **Milestone Project 1: Real-Time Whale & DEX Alert Indexer**

### Month 6: Solidity Engineering & EVM Bytecode Internals (Days 151–180)
- [ ] **Days 151–158**: Hand-Written Solidity (ERC-20, Vaults, Access Control, Escrows without OpenZeppelin)
- [ ] **Days 159–166**: EVM 32-Byte Storage Slot Layout Mapping & Packed Structs
- [ ] **Days 167–174**: Raw EVM Opcode Tracing (`SLOAD`, `SSTORE`, `DELEGATECALL`) & EIP-1967 Proxies
- [ ] **Days 175–180**: `day180_disasm.py` — **Capstone: Python EVM Bytecode Disassembler**

---

## Quarter 3: Smart Contract Security & Vulnerability Analysis (Days 181–270)

### Month 7: Foundry Testing, Mainnet Forking & Static Analysis (Days 181–210)
- [ ] **Days 181–188**: Foundry CLI (`cast`, `forge test`, cheatcodes `vm.prank`, `vm.deal`, `vm.warp`)
- [ ] **Days 189–196**: Stateless Fuzzing & Stateful Invariant Testing
- [ ] **Days 197–204**: Slither Static Analysis Triage & Custom Slither Python Detector
- [ ] **Days 205–210**: `test/MainnetFork.t.sol` — **Capstone: Mainnet Fork Simulation with Impersonation**

### Month 8: Smart Contract Vulnerability Mechanics & Wargames (Days 211–240)
- [ ] **Days 211–218**: Single-Function, Cross-Function & Read-Only Reentrancy PoCs
- [ ] **Days 219–226**: Precision Loss, Division-Before-Multiplication & ERC-4626 Vault Inflation
- [ ] **Days 227–233**: Signature Replay, Uninitialized Proxies & Flash-Loan Spot Price Manipulation
- [ ] **Days 234–240**: Complete 10+ Levels of Ethernaut & Damn Vulnerable DeFi

### Month 9: Historical DeFi Hack Reproduction & Root-Cause Post-Mortems (Days 241–270)
- [ ] **Days 241–248**: Execution Call-Trace Forensics (Phalcon / Tenderly)
- [ ] **Days 249–262**: 3 Standalone Foundry Fork Exploit Reproductions
- [ ] **Days 263–270**: `defi_postmortems/` — **Milestone Project 2: 3 Historical Hacks with Root-Cause Writeups**

---

## Quarter 4: Public Proof-of-Work & Job Hunting (Days 271–365)

### Month 10: On-Chain Threat Intelligence & Fund-Flow Forensics (Days 271–300)
- [ ] **Days 271–278**: Entity Clustering Heuristics (Shared funding, deposit reuse, timing)
- [ ] **Days 279–288**: Cross-Chain Bridge & Privacy Mixer Tracing with Graphviz Flow Maps
- [ ] **Days 289–300**: `investigation_01.md` — **Capstone: Formal On-Chain Forensic Investigation Report #1**

### Month 11: Live Competitive Audits & Protocol Threat Modeling (Days 301–330)
- [ ] **Days 301–314**: Competitive Audit Contest #1 (Sherlock / Cantina / Code4rena)
- [ ] **Days 315–324**: Competitive Audit Contest #2 (Lending / Staking / Bridge Architecture)
- [ ] **Days 325–330**: Retrospective Gap Analysis against Winning Warden Findings

### Month 12: Portfolio Consolidation & Targeted Hiring Execution (Days 331–365)
- [ ] **Days 331–342**: Flagship Deliverable Showcase Packaging (Top 5 Projects)
- [ ] **Days 343–352**: Targeted Outreach to 25 Security Leads & Analytics Managers
- [ ] **Days 353–365**: Live Technical Interview Gauntlet (Contract reading, SQL tracing, live drills)
