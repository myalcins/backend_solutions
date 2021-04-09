### Q1 Solution

- [x] Create a function that returns a list of the last points

I used select_related to prevent extra queries and used values() for the output type.
You can look at the get_last_points function in solution/views.py. 

- [x] The idea for an efficient way

The first idea on my mind was caching. Django provides many ways for caching with the cache framework. I could cache to function result through low-level cache API. I chose a different way. I provided to returning the function results in API endpoint and sending the last-modified date in response header through Django conditional views. I've also added a cache-control header with "no_cache=True". 

After these steps, I used the post_save signal for caching the date of the last record on the NavigationRecord model. In this way, when I creating the last-modified header, I prevented extra queries on the database.

This solution helping to prevent unnecessary queries while the response is the same.
