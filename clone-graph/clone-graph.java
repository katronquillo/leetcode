/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    public Node cloneGraph(Node node) {
        if (node == null) {
            return node;
        }

        HashSet<Integer> visited = new HashSet<Integer>(); // Visited nodes
        Deque<Node> stack = new ArrayDeque<Node>(); // Iterative DFS
        Map<Node, Node> copies = new HashMap<Node, Node>(); // Original : Copy

        stack.addLast(node);
        while (stack.size() > 0) {
            Node original = stack.removeLast();

            // Ignore previously visited/copied nodes
            if (visited.contains(original.val)) {
                continue;
            }

            // Mark original node as visited
            visited.add(original.val);

            // Create a copy of this node and save for later
            if (!copies.containsKey(original)) {
                copies.put(original, new Node(original.val));
            }

            Node copy = copies.get(original);

            // Create a copy of this node's neighbours and save for later
            for (Node originalNeighbour : original.neighbors) {
                if (!copies.containsKey(originalNeighbour)) {
                    copies.put(originalNeighbour, new Node(originalNeighbour.val));
                }
                
                // Add copied neighbour to neighbour list
                Node copyNeighbour = copies.get(originalNeighbour);
                copy.neighbors.add(copyNeighbour);

                // Add original neighbour to stack for further copying 
                stack.addLast(originalNeighbour);
            }
        }

        return copies.get(node);
    }
}