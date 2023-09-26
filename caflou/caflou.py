
import os
import requests
import json

class Caflou:

  '''
  Client SDK for Caflou API.
  Your credentials can be found in the Caflou app: Cog wheel > Account Settings > API  (/settings/integration)
  
  Parameters:
    account_id (str): : Not the same as account name! Found in settings. 
    access_token (str): Token generated in Caflou web app.
    api_root_url (str): If your Caflou is running on a custom domain, put it here includind https://
    dry_run (bool): If true, will not send requests that would alter data. Will print them instead.  
  '''
  
  
  def __init__(self,account_id = "", access_token = "", api_root_url = "https://app.caflou.com/api/v1/", dry_run = False) -> object:
    
    self._dry_run = dry_run
    
    self._access_token = access_token
    self._account_id = account_id
    self._api_root_url = api_root_url
    self._headers = {"Authorization": self._access_token}

  def get(self, api_endpoint: str, query = "per=20") -> dict:
    response = requests.get(
      f"{self._api_root_url}{self._account_id}/{api_endpoint}?{query}", 
      headers = self._headers
    )
    res_dict = response.json()
    return res_dict
  
  def post(self, api_endpoint: str, data_dict :dict) -> dict:
    if self._dry_run:
      print(f"Sending POST to {api_endpoint} with\n{json.dumps(data_dict,indent=4)}")
      return None
    response = requests.post(
      f"{self._api_root_url}{self._account_id}/{api_endpoint}", 
      headers = self._headers, 
      json = data_dict
    )
    res_dict = response.json()
    return res_dict
  
  def patch(self, api_endpoint: str, data_dict :dict) -> dict:
    if self._dry_run:
      print(f"Sending PATCH to {api_endpoint} with\n{json.dumps(data_dict,indent=4)}")
      return None
    response = requests.patch(
      f"{self._api_root_url}{self._account_id}/{api_endpoint}", 
      headers = self._headers, 
      json = data_dict
    )
    res_dict = response.json()
    return res_dict
  
  def delete(self, api_endpoint: str) -> dict:
    response = requests.delete(
      f"{self._api_root_url}{self._account_id}/{api_endpoint}", 
      headers = self._headers
    )
    res_dict = response.json()
    return res_dict
  
  
  
if __name__ == "__main__":
  pass
  # You can add your code here. I know, it's messy. 
  # account = ""
  # token = "" 
  # c = Caflou(account, token)
  # print(c.get("")) # Should return "{'version': 1.0}"