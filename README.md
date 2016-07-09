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
>>> reply.people().list()  # list all people in account
>>> reply.campaigns().list(name='campaign-name')  # find campaigns
```


### People endpoint

[Support page](http://support.replyapp.io/article/50-people)

```python
>>> reply.people().list()  # GET | all people
>>> reply.people().list(_id=11111)  # GET | find people by ID
>>> reply.people().list(email='email@example.com')  # GET | find people by email
```

If both ID and email provided - ID will be used.

### Campaigns endpoint

[Support page](http://support.replyapp.io/article/56-campaigns)

```python
>>> reply.campaigns().list()  # GET | all campaigns
>>> reply.campaigns().list(name='campaign-name')  # GET | find campaigns by name
```

### Actions endpoint

[Support page](http://support.replyapp.io/article/51-actions)

### Statistics endpoint

[Support page](http://support.replyapp.io/article/117-statistics)

### Email Accounts endpoint

[Support page](http://support.replyapp.io/article/125-email-accounts)

## Tests

To be done
