import requests

url="https://api.github.com/users/octocat"
response = requests.get(url)
#want to write a post request in python using requests library
post_url = "https://jsonplaceholder.typicode.com/posts"
post_data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}
post_response = requests.post(post_url, json=post_data)
print(post_response.status_code)
print(post_response.json())
# want to write a put request in python using requests library
put_url = "https://jsonplaceholder.typicode.com/posts/1"
put_data = {
    "id": 1,
    "title": "foo",
    "body": "bar",
    "userId": 1
}
put_response = requests.put(put_url, json=put_data)
print(put_response.status_code)
print(put_response.json())
# want to write a delete request in python using requests library
delete_url = "https://jsonplaceholder.typicode.com/posts/1"
# delete_response = requests.delete(delete_url)
# print(delete_response.status_code)
#want to write a patch request in python using requests library
patch_url = "https://jsonplaceholder.typicode.com/posts/1"
patch_data = {
    "title": "foo masbxhq "      

}
patch_response = requests.patch(patch_url, json=patch_data)
print(patch_response.status_code)
print(patch_response.json())
