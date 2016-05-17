from system.core.model import Model

class Message(Model):
    def __init__(self):
        super(Message, self).__init__()
    def show(self,id):
        query = "SELECT users.first_name, users.last_name, author_id, messages.message, messages.created_on AS created_on, messages.id AS message_id FROM messages LEFT JOIN users on users.id = messages.author_id  WHERE recip_id = :user_id ORDER BY created_on DESC"
        values = {'user_id':id}
        messages =  self.db.query_db(query,values)
        combined = []
        for message in messages:
            info = self.show_comments(message['message_id'])
            message.update({'comments':info})
            combined.append(message)
        return combined
    def show_comments(self,message_id):
        query = "SELECT users.first_name, users.last_name, users.id AS user_id, comments.comment, comments.created_on, comments.id AS comment_id, comments.messages_id, author_id FROM comments LEFT JOIN users on users.id = comments.author_id WHERE messages_id = :message_id"
        values = {'message_id':message_id}
        return self.db.query_db(query,values)
    def add(self, post):
        query = "INSERT INTO messages (message, author_id, recip_id, created_on, modified_on) VALUES (:message, :author_id, :recip_id, NOW(), NOW())"
        values = {'message': post['message'], 'author_id' :post['author_id'], 'recip_id':post['recip_id']}
        return self.db.query_db(query,values)
    def add_comment(self, post):
        print post
        query = "INSERT INTO comments (comment, author_id, messages_id, created_on, modified_on) VALUES (:comment, :author_id, :messages_id, NOW(), NOW());"
        values = {'comment': post['comment'], 'author_id' :post['author_id'],'messages_id' :post['message_id']}
        return self.db.query_db(query,values)
