# Anotações sobre experimentação:


## Callbacks
[Documentação:](https://docs.celeryq.dev/en/stable/userguide/canvas.html#callbacks)

Callbacks can be added to any task using the link argument to apply_async:

```python
add.apply_async((2, 2), link=other_task.s())
```
The callback will only be applied if the task exited successfully, and it will be applied with the return value of the parent task as argument.

As I mentioned earlier, any arguments you add to a signature, will be prepended to the arguments specified by the signature itself!

If you have the signature:
```python
sig = add.s(10)
```
then sig.delay(result) becomes:
```python
add.apply_async(args=(result, 10))
```

Now let’s call our add task with a callback using partial arguments:
```python
add.apply_async((2, 2), link=add.s(8))
```
As expected this will first launch one task calculating 2 + 2, then another task calculating 8 + 4.

## O que fazer com isso:
descobrir_rotas_proximos_dias.apply_async(args=(id_empresa), link=fetch_trechos_by_company_id.s())

## [Evite chamadas síncronas entre tarefas](https://docs.celeryq.dev/en/stable/userguide/tasks.html#avoid-launching-synchronous-subtasks)
Having a task wait for the result of another task is really inefficient, and may even cause a deadlock if the worker pool is exhausted.

Make your design asynchronous instead, for example by using callbacks.
