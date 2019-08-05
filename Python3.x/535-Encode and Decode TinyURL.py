# Runtime: 24 ms, faster than 48.24% of Python online submissions for Encode and Decode TinyURL.
# Memory Usage: 11.7 MB, less than 75.96% of Python online submissions for Encode and Decode TinyURL.
class Codec:
    def __init__(self):
        self.url_pair = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl == "" or longUrl is None:
            return ""
        suffix_set = string.ascii_letters + string.digits
        tiny_url = "http://tinyurl.com/".join(random.choice(suffix_set) for _ in range(6))
        self.url_pair[tiny_url] = longUrl
        return tiny_url

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.url_pair.get(shortUrl)


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
