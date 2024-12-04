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
              hljs.COMMENT('%(LINE_COMMENT_BEGIN)s', '%(JS_LINE_COMMENT_END)s'), // Single-line comments
              hljs.COMMENT('%(BLOCK_COMMENT_BEGIN)s', '%(BLOCK_COMMENT_END)s'), // Multi-line comments
              {
                className: 'type', // Match built-in types and modifiers
                match: /%(TYPE_MATCH)s/,
              },
              {
                className: 'type', // Match return types after '->'
                begin: /%(RETURN_TYPE_BEGIN)s/,
                end: /%(TYPE_MATCH)s/,
                excludeBegin: true,
                excludeEnd: false,
              },
              {
                className: 'keyword', // Keywords like 'let', 'fn', etc.
                match: /%(KEYWORDS)s/,
              },
              {
                className: 'function', // Function declarations
                beginKeywords: '%(FUNCTION_KEYWORD)s',
                end: /%(FUNCTION_DECL_END)s/,
                excludeEnd: true,
                contains: [
                  {
                    className: 'title.function',
                    begin: /%(FUNCTION_NAME)s/,
                  },
                  {
                    className: 'params',
                    begin: /%(FUNCTION_ARGS_BEGIN)s/,
                    end: /%(FUNCTION_ARGS_END)s/,
                    contains: [
                      {
                        className: 'variable',
                        begin: /%(VARIABLE)s/,
                      },
                      {
                        className: 'type',
                        match: /%(TYPE_MATCH)s/,
                      },
                    ],
                  },
                ],
              },
              {
                className: 'function.call', // Function calls
                match: /%(FUNCTION_CALL)s/,
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
      
        hljs.registerLanguage('Xenon', hljsGrammar);
      })();
"""