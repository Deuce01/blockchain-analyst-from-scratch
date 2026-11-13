"""
Day 01: Crypto Transaction Ledger & Top Holder Leaderboard
===========================================================
Mode: Strict Cold-Coding (Zero AI Inline Autocompletion)
Official Reference: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

Technical Specification:
------------------------
1. Data Structure:
   - Create a list of raw transaction dictionaries named `SAMPLE_TRANSACTIONS`.
   - Each dictionary must contain:
       * "tx_hash": str (e.g. "0xabc1...")
       * "sender": str (e.g. "0xAlice...")
       * "receiver": str (e.g. "0xBob...")
       * "amount": float (e.g. 2.5)
       * "status": str ("success" or "failed")
   - Populate with at least 6-8 diverse transactions, including:
       * Multiple transactions from the same sender
       * Transferred back and forth
       * At least 2 failed transactions ("status": "failed")

2. Functions to hand-code:
   a. filter_valid_transactions(txs: list[dict[str, Any]]) -> list[dict[str, Any]]:
      - Filters out any transaction where status != "success".

   b. compute_balances(txs: list[dict[str, Any]]) -> dict[str, float]:
      - Deducts amount from sender and adds amount to receiver.
      - Returns a mapping of address to net balance.

   c. get_leaderboard(balances: dict[str, float], top_n: int = 3) -> list[tuple[str, float]]:
      - Sorts addresses by balance descending.
      - Returns the top_n addresses and their balances.

3. Self-Verification Criteria:
   - When run in terminal: `python day01_ledger.py`
   - Assert that failed transactions are excluded from balance math.
   - Assert sum of all net balances in closed-loop ledger equals 0.0.
   - Run `mypy --strict day01_ledger.py` and resolve any type warnings.
"""

from typing import Any

# TODO: Step 1 (Pen & Paper) - Open your notebook and sketch the transaction list and balance math.
# TODO: Step 2 (Cold Coding) - Hand-write your data structures and functions below without AI autocompletion.
# TODO: Step 3 (Self-Verification) - Write your test assertions and run `python day01_ledger.py`.

if __name__ == "__main__":
    pass
