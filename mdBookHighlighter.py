HIGHLIGHT_FILE = """
    (function() {
        const hljsGrammar = function(hljs) {
          return {
            name: 'Xenon',
            aliases: ['xenon', 'xn'],
            keywords: {
              keyword: '%(KEYWORDS_LIST)s',
              literal: '%(LITERALS_LIST)s',
            },
            contains: [
              hljs.COMMENT('%(LINE_COMMENT_BEGIN)s', '%(LINE_COMMENT_END)s'), // Single-line comments
              hljs.COMMENT('%(BLOCK_COMMENT_BEGIN)s', '%(BLOCK_COMMENT_END)s'), // Multi-line comments
              {
                className: 'type', // Match built-in types and modifiers
                begin: /%(TYPE_BEGIN)s/,
                match: /%(TYPE_MATCH)s/,
                end: /%(TYPE_END)s/,
              },
              {
                className: 'keyword', // Keywords like 'let', 'fn', etc.
                match: /%(KEYWORDS)s/,
              },
              {
                className: 'function', // Function declarations
                Match: /%(FUNCTION_CALL)s/,
              },
              {
                className: 'number', // Numbers
                variants: [
                  { begin: /%(DECIMAL_NUMBER)s/ },
                ],
              },
              {
                className: 'string', // Strings
                variants: [
                  { begin: /%(STRING_LITERAL)s/, end: /%(STRING_LITERAL)s/, contains: [hljs.BACKSLASH_ESCAPE] },
                ],
              },
              {
                className: 'variable', // General variables
                begin: /%(VARIABLE)s/,
                relevance: 0, // Lower relevance to avoid overriding others
              },
              {
                className: 'built_in', // Built-in operators and pointers
                match: /%(OPERATORS)s/,
              },
            ],
          };
        };
      
        hljs.registerLanguage('GladosLang', hljsGrammar);
      })();
"""