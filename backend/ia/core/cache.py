class PromptCache:

    def __init__(self):

        self.cache = {}

    def guardar(self, key, valor):

        self.cache[key] = valor

    def obtener(self, key):

        return self.cache.get(key)


prompt_cache = PromptCache()