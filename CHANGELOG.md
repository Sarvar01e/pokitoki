### v104 - 2023-04-06

-   Count question length in tokens instead of characters (#12).
-   Truncate questions that exceed the maximum number of tokens allowed by ChatGPT.

### v99 - 2023-04-06

-   [Image generation](https://github.com/nalgeon/pokitoki#image-generation) via DALL-E 2.

### v93 - 2023-04-04

-   Switched back to HTML parse mode instead of Markdown, but with code formatting.

### v86 - 2023-04-02

-   Switched to Markdown parse mode instead of HTML.

### v83 - 2023-04-01

-   Access [external links](https://github.com/nalgeon/pokitoki#external-links).

### v76 - 2023-03-31

-   Send large answers as [documents](https://github.com/nalgeon/pokitoki#reply-with-attachment).

### v70 - 2023-03-30

-   Custom [AI shortcuts](https://github.com/nalgeon/pokitoki#shortcuts).

### v68 - 2023-03-29

-   GPT-4 support and `openai_model` config property.
-   Support for fine-tuned models (CLI only).
-   Switched from HTTP/2 to HTTP/1.1 to mitigate LocalProtocolError.

### v61 - 2023-03-18

-   Handle [forwarded messages](https://github.com/nalgeon/pokitoki#forwarding) in private chats.
-   `max_history_depth` config property.

### v56 - 2023-03-16

-   Follow-up by reply.

### v46 - 2023-03-15

-   The [version](https://github.com/nalgeon/pokitoki#bot-information) command.

### c29d380 - 2023-03-13

-   Answer in [groups](https://github.com/nalgeon/pokitoki#groups).

### f2c5962 - 2023-03-11

-   Switched from GPT-3 to GPT-3.5.
-   Remember up to 3 previous questions.
-   Async calls to OpenAI.

### 704ad28 - 2023-02-01

Initial release:

-   Uses the GPT-3 (davinci) model, as GPT-3.5 is currently unavailable.
-   Basic chat functionality with limited context (last question only).
