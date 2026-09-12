# Day 6: Decorators and Properties

## Topics Covered

* Decorators
* Wrapper functions
* `*args` and `**kwargs`
* `functools.wraps`
* Decorator factories
* `@property`
* Property getters and setters
* Validation using properties
* Function execution timing
* Retry decorators
* Stacking multiple decorators
* Access control using decorators
* Dispatch and route registration

## Exercises

1. Greeting Decorator using `@shout`
2. Banner Decorator using `@banner`
3. Timer Decorator using `@timer`
4. `Temperature` Class with `@property`
5. Retry Decorator using `@retry`
6. `log_calls` Decorator and Decorator Stacking
7. Access Control using `@requires_role`
8. Validated `BankAccount` Class
9. Admin-only `transfer()` Function

## Challenge Project

### Mini Access-Control System + Validated `BankAccount`

Built a small access-control system using decorators and a validated `BankAccount` class.

The project:

* Created a `@requires_role(role)` decorator factory to control access to protected functions.
* Used `@property` and a setter to validate the bank account balance.
* Implemented `deposit()` and `withdraw()` methods.
* Created an admin-only `transfer()` function.
* Tested the transfer with both an admin user and a regular user.
* Added stretch examples for audit logging, computed properties, and a route registry.


## What I Learned

During Day 6, I learned how decorators can modify or extend the behavior of functions without changing the original function. I learned how wrapper functions work and how `*args` and `**kwargs` allow decorators to work with functions having different arguments.

I learned how `functools.wraps` preserves the original function's metadata when using decorators. I also learned how decorator factories work, especially the three-layer structure used for decorators such as `@retry(times=3, delay=1)` and `@requires_role("admin")`.

I learned how `@property` allows methods to be accessed like attributes and how property setters can be used to validate values before storing them. In the `BankAccount` class, updating `self.balance` automatically triggers the setter and its validation.

I also learned how multiple decorators can be stacked and that the order of stacked decorators affects the order in which they execute.

## Challenges Faced

One challenge was understanding the multiple layers of decorator factories such as `@retry` and `@requires_role`. I learned that the outer function receives the decorator arguments, the middle function receives the original function, and the wrapper executes the protected or modified function.

Another challenge was understanding how `@property` and its setter work together. I learned that using `self.balance = ...` calls the setter automatically, allowing validation to be applied whenever the balance changes.

I also found decorator stacking challenging because the order of decorators changes the execution flow. I learned that decorators are applied from the bottom upward, so changing their order can change which decorator runs first.

Another challenge was understanding how `ops[op](a, b)` and route registries work. I learned that a dictionary can store functions, retrieve a function using a key, and then execute it by passing arguments.
