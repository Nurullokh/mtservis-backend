class OrderStatus:
    NEW = "new"
    CONFIRMED = "confirmed"
    ASSIGNED = "assigned"
    IN_PROCESS = "in_process"
    DONE = "done"

    choices = (
        (NEW, NEW),
        (CONFIRMED, CONFIRMED),
        (ASSIGNED, ASSIGNED),
        (IN_PROCESS, IN_PROCESS),
        (DONE, DONE),
    )
