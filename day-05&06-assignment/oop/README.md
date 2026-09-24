# Day 6: Object-Oriented Programming (OOP)

## Topics Covered

* Classes and objects
* Instance attributes and methods
* Class attributes
* Constructors
* Encapsulation
* Private attributes
* Inheritance
* Multilevel inheritance
* Polymorphism
* Method overriding
* `super()`
* Class methods
* Alternative constructors
* Abstract classes
* Abstract methods
* `ABC` and `abstractmethod`

## Exercises

### Easy

1. Created a `Book` class with `title`, `author`, and `describe()` method.
2. Used a class attribute `count` to track the number of `Book` objects created.

### Medium

1. Created a `Shape` base class with `Circle` and `Rectangle` subclasses and demonstrated polymorphism using the `area()` method.
2. Created a `BankAccount` class with a private `__balance` and implemented `deposit()`, `withdraw()`, and `get_balance()` methods with validation.
3. Created a `Book.from_string()` class method as an alternative constructor.

### Hard

1. Implemented multilevel inheritance using `Vehicle → Car → SportsCar` and used `super()` in each constructor.
2. Created an abstract `PaymentMethod` class and implemented `CreditCard`, `Esewa`, and `MobileBanking` subclasses using polymorphism.

## Challenge Project

### Mini Library Management System

Built a mini library management system to practice the four pillars of Object-Oriented Programming.

The project includes:

* Created an abstract `LibraryItem` class with an abstract `describe()` method.
* Used inheritance to create `Book`, `DVD`, and `Magazine` classes.
* Used polymorphism by overriding `describe()` for each library item.
* Used a protected `_checked_out` attribute to track item availability.
* Created a `Member` class with a private `__borrowed_items` list.
* Implemented `borrow()` and `return_item()` methods with validation.
* Created a `Library` class to manage library items and members.
* Implemented `checkout()` to update the item's checkout status and the member's borrowed items.
* Added `Library.from_catalog()` as an alternative constructor using `@classmethod`.
* Added validation for attempting to borrow an already checked-out item.


## What I Learned

During Day 6, I learned the fundamentals of Object-Oriented Programming and how classes and objects are used to model real-world entities.

I learned about instance attributes, class attributes, constructors, instance methods, and class methods. I also practiced using private attributes to achieve encapsulation and protect data from direct access.

I learned how inheritance allows a class to reuse and extend the functionality of another class. I practiced multilevel inheritance and used `super()` to initialize attributes from parent classes.

I also learned polymorphism through method overriding, where different subclasses provide their own implementation of the same method.

Finally, I learned about abstraction using `ABC` and `abstractmethod`. Abstract classes define a common interface that subclasses must implement.

## Challenges Faced

One challenge was understanding the difference between instance attributes and class attributes, especially when using a class attribute to count the number of objects created.

Another challenge was understanding how private attributes such as `__balance` and `__borrowed_items` provide encapsulation and how methods can be used to safely access or modify them.

I also found multilevel inheritance and `super()` challenging at first. I learned how each class can initialize its own attributes while also calling the constructor of its parent class.

Understanding polymorphism and method overriding was another challenge. I learned that different subclasses can implement the same method differently while allowing objects to be processed through a common interface.

The challenge project helped me understand how encapsulation, inheritance, polymorphism, and abstraction can work together in a practical application.
