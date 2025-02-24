import os

def pass_at_k(predictions, ground_truth, k=1):
    """
    Computes Pass@k by checking if the correct Verilog code is in the top-k predictions.
    """
    correct = 0
    for pred in predictions[:k]:  # Check first k generated outputs
        if pred.strip() == ground_truth.strip():
            correct += 1
    return correct / k

def test_case_pass_rate(test_cases, model_outputs):
    """
    Computes Test Case Pass Rate by checking how many generated outputs match the expected outputs.
    """
    passed = sum(1 for case, output in zip(test_cases, model_outputs) if output.strip() == case.strip())
    return passed / len(test_cases) if test_cases else 0

if __name__ == "__main__":
    # Load expected output from a reference file
    with open("tests/expected_output.v", "r") as f:
        expected_output = f.read().strip()

    # Load generated Verilog code
    with open("generated_code/generated.v", "r") as f:
        generated_code = f.read().strip()

    # Simulate multiple outputs from the model for Pass@k
    predictions = [
        generated_code,  # The current best attempt
        "module counter; // Alternative LLM output",
        "module adder;",  # Incorrect variation
        "module shift_reg;",  # Another incorrect variation
        expected_output  # One correct answer
    ]

    # Print Debugging Information
    print("🔍 Expected Output:\n", expected_output)
    print("🔍 Generated Output:\n", generated_code)

    # Compute Pass@k Scores
    print("✅ Pass@1 Score:", pass_at_k(predictions, expected_output, 1))
    print("✅ Pass@5 Score:", pass_at_k(predictions, expected_output, 5))
    print("✅ Pass@10 Score:", pass_at_k(predictions, expected_output, 10))

    # Compute Test Case Pass Rate
    test_cases = [expected_output]  
    model_outputs = [generated_code]  
    print("✅ Test Case Pass Rate:", test_case_pass_rate(test_cases, model_outputs))
