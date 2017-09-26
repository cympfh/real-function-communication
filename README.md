# real-function-communication

## self-speaking

Given a real-function by its samples, for example,

- `double it`
    - 1 `->` 2
    - 2 `->` 4
    - 10 `->` 20

Generator, `G` understands the function by its samples, and can generate
the expression by language (an array of tokens), for example, "double it."

Interpreter, `I` understands the language expression as a real-function.

- `G: [(X, Y)] -> [Token]`
- `I: [Token] -> (X -> Y)`
    - where
        - `X` and `Y` are the set of real numbers

