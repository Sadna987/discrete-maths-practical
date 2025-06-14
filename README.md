# **Practical List - Set, Relation, Graph & Permutation Programs**

## **Introduction**
This repository contains Python programs that demonstrate fundamental concepts in **Set Operations, Relations, Graph Theory, and Permutations**. Each program is menu-driven and allows users to perform various operations interactively.

---

## **1. Set Operations (`SET` Class)**
### **Features Implemented:**
- **`ismember(element)`**: Checks whether an element belongs to the set.
- **`powerset()`**: Lists all subsets (power set) of the given set.
- **`subset(set2)`**: Checks if one set is a subset of another.
- **`union(set2)`**: Finds the union of two sets.
- **`intersection(set2)`**: Finds the intersection of two sets.
- **`complement(universal_set)`**: Computes the complement using a universal set.
- **`set_difference(set2)`**: Finds elements in the first set but not in the second.
- **`symmetric_difference(set2)`**: Finds elements exclusive to either set.
- **`cartesian_product(set2)`**: Computes the Cartesian product of two sets.

### **Usage Instructions:**
1. Run the program.
2. Select an operation from the menu.
3. Provide the required input (e.g., set elements).
4. View the computed result.

---

## **2. Relation (`RELATION` Class)**
### **Implemented Features (Using Matrix Representation):**
- **`reflexive()`**: Checks if the relation is reflexive.
- **`symmetric()`**: Checks if the relation is symmetric.
- **`antisymmetric()`**: Checks if the relation is anti-symmetric.
- **`transitive()`**: Checks if the relation is transitive.
- **`equivalence_relation()`**: Determines if the relation is an equivalence relation.
- **`partial_order_relation()`**: Determines if the relation forms a partial order.

### **Usage Instructions:**
1. Enter the adjacency matrix representation of the relation.
2. Choose the desired property check from the menu.
3. View the output determining reflexivity, symmetry, and transitivity.

---

## **3. Permutations**
### **Implemented Features:**
- Generates **all possible permutations** of a set of digits.
- Supports **both repetition and non-repetition**.

### **Usage Instructions:**
1. Provide the input set of numbers.
2. Choose whether repetition is allowed.
3. View all possible permutations.

---

## **4. Polynomial Evaluation**
### **Implemented Features:**
- Stores polynomial **f(n) = 4n² + 2n + 9** in an array.
- Computes **f(n) for any user-provided value of `n`**.

### **Usage Instructions:**
1. Enter a value for `n`.
2. View the evaluated polynomial result.

---

## **5 & 6. Graph Completeness**
### **Implemented Features:**
- **Adjacency Matrix Representation**: Checks whether a graph is complete.
- **Adjacency List Representation**: Alternative method for completeness check.

### **Usage Instructions:**
1. Provide the graph representation (matrix or list).
2. Choose the completeness check operation.
3. View whether the graph is complete or not.

---

## **7. Graph Degree Analysis**
### **Implemented Features:**
- Computes **in-degree** and **out-degree** for each vertex.

### **Usage Instructions:**
1. Enter the **adjacency matrix representation** of the directed graph.
2. View the calculated **in-degree and out-degree** for each vertex.

---

