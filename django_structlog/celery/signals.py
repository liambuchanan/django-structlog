import django.dispatch


bind_extra_task_metadata = django.dispatch.Signal()
""" Signal to add extra ``structlog`` bindings from ``celery``'s task.

>>> from django.dispatch import receiver
>>> from django_structlog.celery import signals
>>>
>>> @receiver(signals.bind_extra_task_metadata)
... def receiver_bind_extra_request_metadata(sender, signal, task=None, logger=None):
...     logger.bind(correlation_id=task.request.correlation_id)

"""


modify_context_before_task_publish = django.dispatch.Signal()
""" Signal to modify context passed over to ``celery`` task's context. You must modify the ``context`` dict.

>>> from django.dispatch import receiver
>>> from django_structlog.celery import signals
>>>
>>> @receiver(signals.modify_context_before_task_publish)
... def receiver_modify_context_before_task_publish(sender, signal, context):
...     keys_to_keep = {"request_id", "parent_task_id"}
...     new_dict = {
...         key_to_keep: context[key_to_keep]
...         for key_to_keep in keys_to_keep
...         if key_to_keep in context
...     }
...     context.clear()
...     context.update(new_dict)

"""

pre_task_succeeded = django.dispatch.Signal()
""" Signal to add ``structlog`` bindings from ``celery``'s successful task.

>>> from django.dispatch import receiver
>>> from django_structlog.celery import signals
>>>
>>> @receiver(signals.pre_task_succeeded)
... def receiver_pre_task_succeeded(sender, signal, logger=None, result=None):
...     logger.bind(result=str(result))

"""
