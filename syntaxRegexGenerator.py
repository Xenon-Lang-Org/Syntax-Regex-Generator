keywords = ["let", "fn", "while", "if", "elif", "else", "return", "type"]
literals = ["true", "false"]

function_keyword = "fn"

var_name = "[a-zA-Z_][a-zA-Z0-9_]*"
custom_type_name = "[A-Z][a-zA-Z0-9_]*"

regex_dict = {
    "LINE_COMMENT_BEGIN" : "//",
    "LINE_COMMENT_END" : "\\n",
    "JS_LINE_COMMENT_END" : "$",
    "BLOCK_COMMENT_BEGIN" : "/\\\\*",
    "BLOCK_COMMENT_END" : "\\\\*/",
    "STRING_LITERAL" : "\\\"",
    "CHAR_LITERAL" : "'",
    "ESCAPE_CHAR" : "\\\\\\\\.",
    "DECIMAL_NUMBER" : "\\\\b[0-9]+[.]?[0-9]*\\\\b",
    "KEYWORDS" : f"\\\\b({'|'.join(keywords)})\\\\b",
    "TYPE_BEGIN" : "(->\\\\s*)?",
    "TYPE_MATCH" : f":?\\\\s*(\\\\*?\\\\s*(mut\\\\s+)?)*\\\\b(i8|i16|i32|i64|u8|u16|u32|u64|f32|f64|bool|char|void|{custom_type_name})\\\\b",
    "TYPE_END" : ".*",
    "FUNCTION_NAME": f"\\\\b{var_name}\\\\b",
    "FUNCTION_CALL" : f"\\\\b({var_name})\\\\s*\\\\(",
    "FUNCTION_DECL_BEGIN" : "\\bfn\\b",
    "FUNCTION_DECL_END" : "\\{",
    "FUNCTION_ARGS_BEGIN" : "\\(",
    "FUNCTION_ARGS_END" : "\\)",
    "OPERATORS" : "@|&",
    "VARIABLE" : f"\\\\b{var_name}\\\\b",
    "LITERALS" : f"\\\\b({'|'.join(literals)})\\\\b"
}

list_dict = {
    "KEYWORDS_LIST" : ' '.join(keywords),
    "LITERALS_LIST" : ' '.join(literals)
}

kw_dict = {
    "FUNCTION_KEYWORD" : function_keyword
}


from vscodeHighlighter import VSCODE_FILE
from mdBookHighlighter import HIGHLIGHT_FILE

with open("xenon.tmLanguage.json", "w") as f:
    f.write(VSCODE_FILE % regex_dict)

# replace all \\ with \ in the dict apart if key contains "_COMMENT_"
# this is because hljs on the docs repo uses comment regex as "string" and not js regex like /regex/
for key in regex_dict:
    if "_COMMENT_" not in key:
        regex_dict[key] = regex_dict[key].replace("\\\\", "\\")

with open("xenonHighlighter.js", "w") as f:
    f.write(HIGHLIGHT_FILE % {**regex_dict, **list_dict, **kw_dict})