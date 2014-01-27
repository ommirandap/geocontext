Notes
=====

## Important fields from **Twitter-JSON**

### Important fields from [TWEETS][ref2]

- **[coordinates][ref5]** -> geographic location of this tweet ([geoJSON][ref3])
- **created_at** -> UTC time of the tweet
- **geo** -> *deprecated* Everyone should use *coordinates* now
- **id_str** -> Tweet ID
- **lang** -> Machine detected language identifier of the tweet
- **place** -> Indicates the tweet is **associated** (not necessarily originated from) a [Place][ref4]
- **text** -> Text Tweet itself
- **user** -> Yes, reference to the user who posted this Tweet. Follows the structure describe next

### Important Fields from [USERS][ref1]
#### Why Users? Because the JSON's tweet, has a user object in it

- **description** -> User's BIO
- **geo_enabled** -> true if the user has activated the posibility of geotagging their tweets
- **id_str** -> User id
- **lang** -> Machine detected language of the user
- **location** -> User-defined location 
- **time_zone** -> String describing the Time Zone the user define
- **utc_offset** -> The offset from GMT/UTC in seconds


 [ref1]: https://dev.twitter.com/docs/platform-objects/users
 [ref2]: https://dev.twitter.com/docs/platform-objects/tweets
 [ref3]: http://www.geojson.org
 [ref4]: https://dev.twitter.com/docs/platform-objects/places#obj-boundingbox
 [ref5]: https://dev.twitter.com/docs/platform-objects/tweets#obj-coordinates