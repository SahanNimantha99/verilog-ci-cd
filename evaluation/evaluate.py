import os

def pass_at_k(predictions, ground_truth, k=5):
    correct = 0
    for pred in predictions[:k]:
        if pred.strip() == ground_truth.strip():
            correct += 1
    return correct / k

def test_case_pass_rate(test_cases, model_outputs):
    passed = sum(1 for case, output in zip(test_cases, model_outputs) if output.strip() == case.strip())
    return passed / len(test_cases)

if __name__ == "__main__":
    # Load expected output from a reference file
    with open("tests/expected_output.v", "r") as f:
        expected_output = f.read()

    # Load generated Verilog code
    with open("generated_code/generated.v", "r") as f:
        generated_code = f.read()

    predictions = [
        generated_code,  
        "module counter; // Alternative LLM output",
        "module adder;",  
    ]

    print("✅ Pass@5 Score:", pass_at_k(predictions, expected_output, 5))

    test_cases = [expected_output]  
    model_outputs = [generated_code]  
    print("✅ Test Case Pass Rate:", test_case_pass_rate(test_cases, model_outputs))
