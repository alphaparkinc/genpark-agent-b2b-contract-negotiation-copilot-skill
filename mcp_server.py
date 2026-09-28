import sys
import json
from client import ContractNegotiationCopilot

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "evaluate_counter_offer",
                        "description": "Evaluates client/vendor counter-offers and generates optimal give-get terms.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "initial_quote": {"type": "number"},
                                "counter_offer": {"type": "number"},
                                "contract_months": {"type": "integer"}
                            }
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        args = params.get("arguments", {})
        copilot = ContractNegotiationCopilot()
        res = copilot.evaluate_counter_offer(
            args.get("initial_quote", 120000.0),
            args.get("counter_offer", 95000.0),
            args.get("contract_months", 24)
        )
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "content": [{"type": "text", "text": json.dumps(res, indent=2)}]
            }
        }
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    copilot = ContractNegotiationCopilot()
    print(json.dumps(copilot.evaluate_counter_offer(), indent=2))

if __name__ == "__main__":
    main()
