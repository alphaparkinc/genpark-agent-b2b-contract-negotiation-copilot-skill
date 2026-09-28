from client import ContractNegotiationCopilot

copilot = ContractNegotiationCopilot()
res = copilot.evaluate_counter_offer(120000.0, 95000.0, 24)
print("=== B2B Negotiation Copilot Strategy ===")
print("Requested Discount:", f"{res['discount_requested_pct']}%")
print("Recommended Counter:", f"${res['recommended_quote']:,.2f}")
print("Strategy:", res["strategy"])
print("Condition Required:", res["condition"])
