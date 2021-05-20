__all__ = ['IntegreSQLError', 'TemplateAlreadyInitialized', 'ManagerNotReady', 'TemplateNotFound', 'DatabaseDiscarded']


class IntegreSQLError(Exception):
    pass


class TemplateAlreadyInitialized(IntegreSQLError):
    pass


class ManagerNotReady(IntegreSQLError):
    pass


class TemplateNotFound(IntegreSQLError):
    pass


class DatabaseDiscarded(IntegreSQLError):
    pass
