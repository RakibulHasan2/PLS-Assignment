# PLS-Assignment

## 1. Primitive Data Types
Description:
Primitive data types are the basic building blocks in programming languages. They represent the simplest form of data.

- Integer: Whole numbers, either positive or negative.
- Float: Floating-point numbers, used to represent real numbers with a decimal.
- String: Multiple letter or symbol, typically represented by a character literal.
- Boolean: Represents true or false.

- Output:<br>
![alt text](image-7.png)

## 2. Design Issues of Character String Types, strings and their operations, string length options, evaluation and implementation with code.

- Should strings be a special kind of character array or a primitive type?
  > Character Arrays: Strings as arrays of characters, offering more control but requiring manual memory management.<br>
  > Primitive Type: Strings as built-in types, with automatic memory management and easier operations, but sometimes less efficient.

- Should strings have static or dynamic length?
  > Static Length: Fixed size, determined at compile-time, more memory-efficient but less flexible.<br>
  > Dynamic Length: Can change size during runtime, more flexible but with potential performance overhead.

- String Operations and Length Options
  > Operations: Concatenation, substring extraction, length calculation, and comparison.
  > Length Options:
    - Fixed-Length: Set size, can’t grow or shrink (used in languages like C).
    - Dynamic-Length: Flexible size, adjusts as needed (used in languages like Python).

- Output: <br>
![alt text](image-1.png)

## 3.Answer the design issues of enumeration, implement enum with code and evaluation.
Design Issues of Enumeration Types
- Can an enumeration constant appear in more than one type definition?
Typically, enumeration constants are scoped to a specific enum type. If reused across types, type-checking is required to ensure the constant is used in the correct context.

- Are enumeration values coerced to integer?
In most languages (like C, C++, and Python), enum values are internally represented as integers, but they can be accessed using their symbolic names.

- Are other types coerced to an enumeration type?
Generally, values of other types (e.g., integers or strings) are not automatically coerced into an enum type unless explicitly converted. Some languages (like C++) may allow implicit conversion in certain cases, but it is not common.

- Output:<br>
![alt text](image-2.png)

## 4. Answer the design issues of the array types and briefly described subscript bindings and array categories.
- What types are legal for subscripts?
Generally, subscripts must be of integer types, but some languages allow other types, such as strings or floating-point numbers. For example, Python allows negative indices, while languages like C require integer or integer-like types for subscripts.

- Are subscripting expressions in element references range-checked?
In some languages (e.g., Python, Java), subscripting is range-checked at runtime, meaning an error occurs if you access an out-of-bounds index. In languages like C, subscripting is not range-checked, and accessing out-of-bounds indices can lead to undefined behavior.

- When are subscript ranges bound?
Subscript ranges are bound at either compile-time (for static arrays) or runtime (for dynamic arrays). In statically typed languages like C, the size of an array is typically fixed at compile-time, while dynamically-typed languages (e.g., Python) allow dynamic resizing during runtime.

- When does array allocation take place?
In languages like C, arrays can be allocated at compile-time for static arrays or at runtime for dynamic arrays. In high-level languages (e.g., Python, Java), arrays are dynamically allocated at runtime.

- Are ragged or rectangular multidimensional arrays allowed, or both?
Rectangular arrays have the same number of elements in each row. Ragged arrays allow different numbers of elements in each row. Some languages (e.g., C, Python) support both, while others may only support rectangular arrays.

- Can arrays be initialized when they have their storage allocated?
Yes, most languages allow array initialization at the time of storage allocation. For example, C allows initializing arrays at declaration, while languages like Python provide automatic initialization to default values.

- What kinds of slices are allowed, if any?
Many languages (e.g., Python) allow slicing, which lets you access a part of an array or list. For example, you can extract a subarray from a larger array using slice syntax (array[start:end]).

- Subscript Bindings and Array Categories
> Subscript Binding: Refers to the association between an index (subscript) and the actual memory location of an array element.
> Static Arrays: Subscripts are bound at compile-time. The array size and indices are fixed.
> Dynamic Arrays: Subscripts are bound at runtime, allowing the array size to change during program execution.

- Array Categories:
> One-Dimensional Arrays: Simple list-like structures, where each element is accessed via a single index.
> Multidimensional Arrays: Arrays with more than one index (e.g., 2D arrays), typically used for matrix-like structures.
> Ragged Arrays: Arrays of arrays where each subarray can have a different size (e.g., arrays of lists in Python).
Rectangular Arrays: Arrays with uniform size in all dimensions.

- Output:<br>
![alt text](image-3.png)

## 5. Describe design issues and evaluation of record types.
- Design Issues:
> Storage: How the records are stored in memory (contiguous or scattered).
> Field Names: How to handle field names (global vs. scoped).
> Efficiency: Performance when accessing specific fields of a record.

- Output:<br>
![alt text](image-4.png)

## 6. Describe design issues, implement union with code and evaluation of union types.
- Design Issues:
> Storage: How to store data of different types in a single memory location.
> Type Safety: Ensuring that only one type is used at a time.
> Size: A union typically uses the memory size of its largest member.

- Output:<br>
![alt text](image-5.png)

## 7. Describe design issues, implement pointers in c and c++ with code.

- What are the scope and lifetime of a pointer variable?
> Scope: The scope of a pointer variable refers to where in the program it can be accessed. Pointers can be local (within a function), global (accessible throughout the program), or dynamic (depending on how memory is allocated). <br>  
> Lifetime: The lifetime of a pointer is determined by the scope of the pointer variable. For example, if a pointer is declared inside a function, its lifetime ends when the function exits. However, a pointer to dynamically allocated memory (e.g., malloc in C, new in C++) will persist until explicitly freed.

- What is the lifetime of a heap-dynamic variable (the value a pointer references)?
> The lifetime of a heap-dynamic variable (i.e., a variable allocated in the heap) lasts until the memory is explicitly deallocated using commands like free() in C or delete in C++. It exists independently of the scope of the pointer itself, so it persists even if the pointer goes out of scope.

- Are pointers restricted as to the type of value to which they can point?
> Type Safety: In languages like C and C++, pointers are typically type-specific, meaning that a pointer of type int* can only point to a variable of type int. However, void pointers (void*) can point to any data type, but the actual type must be cast back before dereferencing.
Type safety ensures that the pointer only points to a compatible type, preventing access to invalid memory locations.

- Are pointers used for dynamic storage management, indirect addressing, or both?
> Dynamic Storage Management: Pointers are widely used for dynamic memory allocation. Using malloc in C or new in C++, pointers can allocate memory at runtime, which is useful for building complex data structures like linked lists, trees, and graphs.<br>
> Indirect Addressing: Pointers are also used for indirect addressing, where the pointer holds the memory address of a value, and dereferencing the pointer allows access to the value itself.

- Should the language support pointer types, reference types, or both?
> Pointer Types: Languages like C and C++ provide explicit pointer types (int*, float*, etc.) to allow low-level memory management and manipulation.<br>
> Reference Types: Languages like C++ also support references, which are safer than pointers because they don't need to be dereferenced and cannot be NULL. A reference is an alias for another variable and can’t be reseated to point to something else after initialization.

- Output:<br>
![alt text](image-6.png)