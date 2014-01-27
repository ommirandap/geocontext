# BD info

## Tables

- ### breakingnews
	- event (8521)
	- eventfeatures (0)
	- tweet (16M aprox)
	- tweetfeatures (16M aprox)
	- user (5.5M aprox)

## Descripcion

- ### tweet (table)
	- **tweet_id (PK)**
	- text
	- **in_reply_to_status_id**
	- favorite_count
	- source
	- coordinates
	- entities
	- in_reply_to_screen_name
	- **in_reply_to_user_id**
	- retweet_count
	- is_retweet
	- **retweet_of_id (MUL)**
	- **user_id_id (MUL)**
	- lang
	- created_at
	- **event_id_id (MUL)**

- ### tweetfeatures
	- **id (PK)**
	- **tweet_id_id (MUL)**
	- ...
	- sentiment_score_pos
	- sentiment_score_neg
	- sentiment_category

- ### user
	- **user_id (PK)**
	- verified
	- geo_enabled
	- entities
	- followers_count
	- location
	- utc_offset
	- statuses_count
	- name
	- lang
	- screen_name
	- url
	- created_at
	- time_zone
	- listed_count
	- friends_count

- ### event
	- **id (PK)**
	- keywords
	- datetime
	- featured

- ### eventfeatures
	- No tiene ningun elemento, ademas no es relevante para nuestros propósitos