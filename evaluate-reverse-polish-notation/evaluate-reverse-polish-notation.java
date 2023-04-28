class Solution {
    public int evalRPN(String[] tokens) {
        List<String> operators = Arrays.asList("+", "-", "*", "/");
        Stack<Integer> stack = new Stack<>();

        // Iterate through tokens
        for (String token : tokens) {
            if (operators.contains(token)) {
                int rightOperand = stack.pop();
                int leftOperand = stack.pop();

                int result;
                if (token.equals("+")) {
                    result = leftOperand + rightOperand;
                }
                else if (token.equals("-")) {
                    result = leftOperand - rightOperand;
                }
                else if (token.equals("*")) {
                    result = leftOperand * rightOperand;
                }
                else {
                    result = leftOperand / rightOperand;
                }
                stack.push(result);
            }
            else {
                stack.push(Integer.parseInt(token));
            }
        }

        return stack.pop();
    }
}