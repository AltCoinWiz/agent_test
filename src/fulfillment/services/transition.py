def is_newer(event,current):
    return current is None or event.sequence > current.sequence
