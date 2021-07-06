# Logging Handlers
Multiple handlers for logging in a single module

> Note that `rootLogger` cannot be set to levels `DEBUG` or `INFO` since a similar level `[DEBUG]` is already used in 
> `consoleLogger` which is another `StreamHandler`