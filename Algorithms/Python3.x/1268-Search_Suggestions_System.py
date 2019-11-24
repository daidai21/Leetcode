class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        result = []
        for i in range(1, len(searchWord) + 1):
            products = list(filter(lambda x: x.startswith(searchWord[:i]), products))
            result.append(products[:3])
        return result
