# Replyapp Python API Wrapper

| Author | Email |
| --- | --- |
| Dmytro Soloviov | [dmytro.soloviov@gmail.com](mailto:dmytro.soloviov@gmail.com) |

Replyapp.io public API wrapper.

## Requirements

- [Python 2.7](https://www.python.org)
- [Requests](http://docs.python-requests.org/en/master/)

## Usage

```python
>>> from reply import Reply
>>> reply = Reply('your-api-key')
>>> reply.people.list.all()  # list all people in account
>>> reply.campaigns.list.name('campaign-name')  # find campaigns by name
```


### People endpoint

[Support page](http://support.replyapp.io/article/50-people)

```python
>>> # GET methods
>>> reply.people.list.all()  # list all people
>>> reply.people.list.id(11111)  # find people by ID
>>> reply.people.list.email('email@example.com')  # find people by email
```

### Campaigns endpoint

[Support page](http://support.replyapp.io/article/56-campaigns)

```python
>>> # GET methods
>>> reply.campaigns.list.all()  # list all campaigns
>>> reply.campaigns.list.name('campaign-name')  # find campaigns by name
```

### Actions endpoint

[Support page](http://support.replyapp.io/article/51-actions)

### Statistics endpoint

[Support page](http://support.replyapp.io/article/117-statistics)

### Email Accounts endpoint

[Support page](http://support.replyapp.io/article/125-email-accounts)

## Tests

```shell
$ python -m unittest discover -v
```

