// Runtime: 1288 ms, faster than 5.24% of C++ online submissions for Implement Trie (Prefix Tree).
// Memory Usage: 85.8 MB, less than 6.67% of C++ online submissions for Implement Trie (Prefix Tree).
class Trie {
public:
    /** Initialize your data structure here. */
    Trie() {
        // pass
    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        mem.push_back(word);
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        for (string w : mem)
            if (w == word)
                return true;
        return false;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        for (string w : mem) {
            if (w.size() >= prefix.size()) {
                string tmp = w.substr(0, prefix.size());
                if (tmp == prefix)
                    return true;
            }
        }
        return false;
    }
private:
    vector<string> mem;
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */




// Runtime: 72 ms, faster than 76.13% of C++ online submissions for Implement Trie (Prefix Tree).
// Memory Usage: 44.8 MB, less than 56.67% of C++ online submissions for Implement Trie (Prefix Tree).
class TrieNode {
  public:
    TrieNode *next[26];
    bool is_word;

    TrieNode(bool b = false) {
        memset(next, 0, sizeof(next));
        is_word = b;
    }
};


class Trie {
public:
    TrieNode* root;
    /** Initialize your data structure here. */
    Trie() {
        root = new TrieNode();
    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        TrieNode* p = root;
        for (char ch : word) {
            if (p->next[ch - 'a'] == NULL)
                p->next[ch - 'a'] = new TrieNode();
            p = p->next[ch - 'a'];
        }
        p->is_word = true;
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        TrieNode* p = find_node(word);
        return p != NULL && p->is_word;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        return find_node(prefix) != NULL;
    }
private:
    TrieNode* find_node(string word) {
        TrieNode *p = root;
        for (int i = 0; i < word.size() && p != NULL; ++i)
            p = p->next[word[i] - 'a'];
        return p;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */