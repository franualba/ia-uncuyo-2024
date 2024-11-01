import pandas as pd
from math import log2

class DecisionTree:
    def __init__(self):
        self.tree = None
    
    def calculate_entropy(self, examples: pd.DataFrame) -> float:
        """Calculate entropy for a set of examples."""
        class_counts = examples['play'].value_counts()
        total = len(examples)
        entropy = 0
        for count in class_counts:
            probability = count / total
            entropy -= probability * log2(probability)
        return entropy
    
    def calculate_information_gain(self, examples: pd.DataFrame, attribute: str) -> float:
        """Calculate information gain for an attribute."""
        entropy_before = self.calculate_entropy(examples)
        values = examples[attribute].unique()
        total = len(examples)
        entropy_after = 0
        
        for value in values:
            subset = examples[examples[attribute] == value]
            weight = len(subset) / total
            entropy_after += weight * self.calculate_entropy(subset)
        
        return entropy_before - entropy_after
    
    def plurality_value(self, examples: pd.DataFrame) -> str:
        """Return the most common output value among examples."""
        if len(examples) == 0:
            return None
        return examples['play'].mode()[0]
    
    def learn_decision_tree(self, examples: pd.DataFrame, attributes: list, parent_examples: pd.DataFrame = None) -> dict:
        """Implementation of the LEARN-DECISION-TREE algorithm."""
        if len(examples) == 0:
            return {
                'type': 'leaf',
                'value': self.plurality_value(parent_examples if parent_examples is not None else examples)
            }
        
        if len(examples['play'].unique()) == 1:
            return {
                'type': 'leaf',
                'value': examples['play'].iloc[0]
            }
        
        if len(attributes) == 0:
            return {
                'type': 'leaf',
                'value': self.plurality_value(examples)
            }
        
        importance_scores = {attr: self.calculate_information_gain(examples, attr) 
                           for attr in attributes}
        A = max(importance_scores.items(), key=lambda x: x[1])[0]
        
        tree = {
            'type': 'internal',
            'attribute': A,
            'branches': {}
        }
        
        for value in examples[A].unique():
            exs = examples[examples[A] == value]
            remaining_attributes = [attr for attr in attributes if attr != A]
            subtree = self.learn_decision_tree(exs, remaining_attributes, examples)
            tree['branches'][value] = subtree
        
        return tree
    
    def train(self, data: pd.DataFrame) -> dict:
        """Train the decision tree."""
        attributes = [col for col in data.columns if col != 'play']
        self.tree = self.learn_decision_tree(data, attributes)
        return self.tree
    
    def predict(self, example: pd.Series) -> str:
        """Make a prediction for a single example."""
        node = self.tree
        while node['type'] == 'internal':
            value = example[node['attribute']]
            node = node['branches'][value]
        return node['value']

    def visualize_tree(self, node=None, prefix="", is_last=True, depth=0):
        """
        Create a text-based visualization of the decision tree.
        
        Args:
            node: Current node in the tree
            prefix: Prefix string for the current line
            is_last: Boolean indicating if this is the last branch at this level
            depth: Current depth in the tree
        """
        if node is None:
            node = self.tree
            print("\nDecision Tree Visualization:")
            print("---------------------------")

        # Define the characters for the tree structure
        branch_vertical = "│   "
        branch_last = "└── "
        branch_other = "├── "
        spacer = "    "

        # Create the current line's prefix
        current_prefix = prefix + (branch_last if is_last else branch_other)
        next_prefix = prefix + (spacer if is_last else branch_vertical)

        if node['type'] == 'leaf':
            print(f"{current_prefix}Play = {node['value']}")
        else:
            print(f"{current_prefix}{node['attribute']}")
            branches = list(node['branches'].items())
            
            for i, (value, subtree) in enumerate(branches):
                # Print the branch value
                print(f"{next_prefix}{branch_last if i == len(branches)-1 else branch_other}value = {value}")
                # Recursively visualize the subtree
                self.visualize_tree(subtree, next_prefix + spacer, i == len(branches)-1, depth + 1)

def main():
    # Load the tennis dataset
    data = pd.read_csv("./tennis.csv")
    
    # Create and train the decision tree
    dt = DecisionTree()
    tree = dt.train(data)
    
    # Visualize the tree
    dt.visualize_tree()
    
    print("\nTesting predictions:")
    print("-------------------")
    
    # Make predictions and calculate accuracy
    correct = 0
    total = len(data)
    
    for idx, row in data.iterrows():
        prediction = dt.predict(row)
        actual = row['play']
        correct += (prediction == actual)
        print(f"Example {idx + 1}: Predicted={prediction}, Actual={actual}")
    
    accuracy = (correct / total) * 100
    print(f"\nAccuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    main()