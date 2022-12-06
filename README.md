# prctyp

experimenting with notation useful for typing processes

initial idea for notation:

```
system (
    scope ("p","q"),
    par (
        par (
            prc (
                delay("t", "=", "1"), (
                    send (msg "a") to (endpoint "p"), (
                        recv (msg "b") from (endpoint "p") within 1, (
                            end.
                        ) after (
                            failed.
                        )
                    )
                )
            ), prc (
                delay("t", "=", "1"), (
                    recv (msg "a") from (endpoint "q"), (
                        delay("t", "<=", "1"), (
                            send (msg "b") to (endpoint "q"), (
                                end.
                            )
                        )
                    ) after (
                        failed.
                    )
                )
            )
        ), par (
            prc (
                buffer (
                    endpoints ("p","q"),
                    empty
                )
            ), prc (
                buffer (
                    endpoints ("q","p"),
                    empty
                )
            )
        )
    )
)
```
