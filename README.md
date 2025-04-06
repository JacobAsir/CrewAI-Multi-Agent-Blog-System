# CrewAI-Multi-Agent-Blog-System

𝗪𝗵𝗮𝘁 𝗶𝘀 𝗖𝗿𝗲𝘄𝗔𝗜?
CrewAI enables the creation of 𝗺𝘂𝗹𝘁𝗶-𝗮𝗴𝗲𝗻𝘁 𝘀𝘆𝘀𝘁𝗲𝗺𝘀 that collaborate to achieve shared objectives. These agents are more than just standalone AI models. The key components of CrewAI include:

𝗔𝗴𝗲𝗻𝘁𝘀: Role-specific AI entities with defined goals, backstories, and tools.
𝗧𝗼𝗼𝗹𝘀: External utilities or APIs that agents can use to perform tasks.
𝗧𝗮𝘀𝗸𝘀: Specific objectives assigned to agents, often requiring collaboration.
𝗖𝗿𝗲𝘄: A collection of agents working together to complete a larger workflow.

𝗪𝗵𝗮𝘁 𝗜 𝗕𝘂𝗶𝗹𝘁: 𝗔 𝗕𝗹𝗼𝗴 𝗖𝗼𝗻𝘁𝗲𝗻𝘁 𝗖𝗿𝗲𝗮𝘁𝗶𝗼𝗻 𝗦𝘆𝘀𝘁𝗲𝗺
Using CrewAI, I developed a 𝗺𝘂𝗹𝘁𝗶-𝗮𝗴𝗲𝗻𝘁 𝘀𝘆𝘀𝘁𝗲𝗺 to automate blog content creation from YouTube videos. The system features two specialized agents working together: a Blog Researcher and a Blog Writer.

𝗛𝗼𝘄 𝗜𝘁 𝗪𝗼𝗿𝗸𝘀

𝗕𝗹𝗼𝗴 𝗥𝗲𝘀𝗲𝗮𝗿𝗰𝗵𝗲𝗿 𝗔𝗴𝗲𝗻𝘁:
𝗚𝗼𝗮𝗹: Extract relevant video content from YouTube based on a given topic.
𝗖𝗮𝗽𝗮𝗯𝗶𝗹𝗶𝘁𝗶𝗲𝘀: Uses the YoutubeChannelSearchTool to search a specific channel. Analyzes and summarizes video content.
𝗢𝘂𝘁𝗽𝘂𝘁: A detailed, three-paragraph report on the topic.

𝗕𝗹𝗼𝗴 𝗪𝗿𝗶𝘁𝗲𝗿 𝗔𝗴𝗲𝗻𝘁:
𝗚𝗼𝗮𝗹: Transform the research into a compelling blog post.
𝗖𝗮𝗽𝗮𝗯𝗶𝗹𝗶𝘁𝗶𝗲𝘀: Summarizes the research output into engaging and accessible content. Outputs the final blog post as a markdown file.
