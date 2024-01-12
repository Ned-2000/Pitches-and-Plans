# The script of the game goes in this file.

# Declare images used by this game.

image old_company = im.FactorScale("old company.jpeg", 2.0)

image brainstorm = im.FactorScale("Brainstorming.jpg", 2.2)

image presenting = im.FactorScale("presenting.jpeg", 1.3)

image executive_summary = "executive-summary-components-l.jpg"

image company_description = "company-description-1.jpeg"

image market_research = "market_research.jpg"

image eight_components = "eight-components-marketing-research.jpg"

image competitor_analysis = "competitor_analysis.jpg"

image product_description = "product_description.jpeg"

image financial_planning = "financial_planning.jpg"

image company_appendix = "company_appendix.png"

image company_organization = "Line-Organizational-Structure-1.png"

image marketing_strategies = "market_strategies.png"

image investors = "know-your-potential-investor.jpg"

image black = "#000"

define y = Character('You', color="#d0d0d0")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    show black

    # These display lines of dialogue.
    
    $ player_name = renpy.input("What is your name?")
    
    $ player_name = player_name.strip()
    
    if player_name == "":
        $ player_name="Steve Tissenbaum"

    play music "Pastel (Piano & Cello).mp3" loop

    show old_company
    with dissolve
        
    "You are an MC named %(player_name)s. You’re the typical business worker at a start-up company named Eco Co."
    
    "Eco Co. is a small business that focuses on promoting sustainability."
    
    "Within a year of its operations Eco Co. had made a number of products to help reduce waste in the environment such as bamboo cutlery, napkins from recycled fabric, edible straws and food wraps, etc."
    
    "You suddenly came up with an idea to create an eco-friendly water bottle, but that idea needs to be proposed to investors in order to gain financial support, and possibly growth for the business."
    
    "Your business idea seems like the perfect startup but you need a business plan to accompany this so you can pitch this idea to investors."

    hide old_company
    with dissolve
    show brainstorm at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)
    with dissolve
    
    "You start off with an executive summary. There are many questions you need to ask yourself:"

    show brainstorm at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5):
        blur 16

    show executive_summary at Position(xpos = 0.5, xanchor=0.5, ypos=0.4, yanchor=0.5):
        zoom 0.8
    
    "Who am I selling to?"
    
    "Why do they need my item?"
    
    "What am I selling?"
    
    "What does this product solve?"
    
    "Who am I competing with?"
    
    "What differentiates me from the rest?"
    
    "You have what you're doing, but do you have why you're doing it? Why are you doing this?"
    
    "Now that you have the basics, it's time to delve deeper."

    hide executive_summary
    
    "A business plan, unlike a business model, has a lot more aspects and details to it."
    
    "When did you establish this company? "
    
    "What is my goal for the future of this business?"
    
    "Where is my company located?"
    
    "Who is the person in charge?"
    
    "How many employees do I need?"
    
    "What is the best product of the company?"
    
    "Now that you have a plan, we need to see if you can afford that plan."
    
    "How much of my revenue do I retain as net income?"
    
    "What’s my ratio of liquidity to debt repayment ability?"
    
    "How often do I collect my invoices?"
    
    "Next up is the company description."

    show company_description at Position(xpos = 0.5, xanchor=0.5, ypos=0.4, yanchor=0.5):
        zoom 0.8
    
    "The mission statement should be inspirational to make others believe in your vision, emotional to captivate readers, grab their interest and explain the reason for the company's existential history."
    
    "The company's history should include the founding date, major milestones, location(s), number of employees, executive leadership roles, and flagship products or service objectives."
    
    "Business objectives should be SMART (specific, measurable, achievable, realistic, and time-bound) and must also be tied to key results."

    hide company_description
    show market_research at Position(xpos = 0.5, xanchor=0.5, ypos=0.4, yanchor=0.5):
        zoom 0.7
    
    "You also have to identify your potential customers."
    
    "This is done by creating target markets, A.K.A. personas that include demographic information such as location, income, age, gender, education, profession, and hobbies."
    
    "We have to identify competing businesses in the market and answer questions on their advertising investments, press coverage, customer service, sales and pricing strategies, and third-party ratings."

    hide market_research
    show product_description at Position(xpos = 0.5, xanchor=0.5, ypos=0.4, yanchor=0.5):
        zoom 0.7
    
    "Outline the benefits, production process, and product life cycle of a company's products or services."

    "It emphasizes unique features and their practical and emotional benefits to customers, as well as any intellectual property rights or patents that protect differentiation."

    "The production process details how existing and new products are created, raw materials are sourced and assembled through manufacturing, and quality control is maintained."

    "The product life cycle includes the time between purchases, upsells and down sells, and plans for research and development."

    hide product_description
    show market_strategies at Position(xpos = 0.5, xanchor=0.5, ypos=0.4, yanchor=0.5):
        zoom 1.3

    "In the next step, the business owner should outline their marketing and sales strategy, including launch plans, growth tactics, and retention strategies."

    " It's also important to highlight what differentiates the business from its competitors and briefly touch on topics such as existing customer segments, value propositions and ideal target markets."

    hide market_strategies
    show financial_planning at Position(xpos = 0.5, xanchor=0.5, ypos=0.4, yanchor=0.5):
        zoom 0.7

    "Compile your business finances."

    "This step emphasizes the importance of preparing a budget and financial plan, even if your business is just starting out."

    "For companies seeking investors, income statements, balance sheets, and other financial figures should be included."

    "It is important to accurately calculate costs, including overhead, to determine a sale price that generates the desired profit level."

    "Underestimating business costs can lead to setting sale prices too low."

    hide financial_planning
    show company_organization at Position(xpos = 0.5, xanchor=0.5, ypos=0.4, yanchor=0.5):
        zoom 1.1

    "Lay out the importance of having a strong management team to turn your business idea into a reality and ensure its continued growth."

    "The section of the plan should highlight the expertise and qualifications of each member of the team."

    "It is also important to consider roles that still need to be hired and the cost of hiring experts to assist operations, such as a bookkeeper, CPAs, or attorneys."

    hide company_organization

    "Be realistic when describing your funding request and include a range of numbers."

    "Selling equity means giving up a portion of the equity in your company, and investors may want to participate in decision-making as well as receive a share of profits."

    "Borrowing money is another way to raise capital, but in order to lower interest costs on the debt, it must be repaid as quickly as possible."

    show company_appendix at Position(xpos = 0.5, xanchor=0.5, ypos=0.4, yanchor=0.5):
        zoom 1.1

    "The next step is to compile a well-organized appendix with information that helps investors in their due diligence and gives you or your employees context."

    "Include deeds, permits, legal docs, certifications, business registries, patents, industry associations, identification numbers, contracts, and purchase orders."

    "Figure out how much you'd need from the investors to make your company successful."

    hide company_appendix

    "Let's move on to the final section, the elevator pitch."

    "An elevator pitch serves as a short summary of an idea/product that is designed to grab attention within a short duration."

    "This method is used when you have little time to make an impression such as when you are networking with investors or potential customers."

    "You'll be pitching your sustainable water bottle to investors so here's an idea on how you'll be doing that."

    show investors at Position(xpos = 0.5, xanchor=0.5, ypos=0.4, yanchor=0.5):
        zoom 0.16

    "The first step is to know who you'll be pitching to."

    "When researching your potential investors its important to consider the following:"

    "The industries they invest, to tailor your pitch to their needs."

    "The stage they invest in, to align yourself with investors at those particular stages of business development."

    "And lastly, their track record to figure if they're the right partner for you."

    hide investors

    "The last advice is to consider how to present yourself."

    "Although your idea and skills matter, your personality and character also plays an important part in pitching your idea."

    "Many investors think about and are interested in partnering with trustworthy and open-minded people as 'most experienced investors look at the people first and the opportunity second.'"

    "Consider how you're presenting yourself and to practice your responses to potential questions or criticisms."

    "Telling a story is also an effective way to persuade investors into your idea."

    "The next advice is to consider how to present yourself."

    "Presenting a real-life scenario of a customer facing a pain point and how your product or service solved it can help investors see the potential in your idea."

    "Telling a story can complement the data presented in spreadsheets and charts and provide a fuller picture of your startup's future, effectively highlighting the opportunity in the market."

    show brainstorm at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)

    "You have a business plan ready to pitch your business idea to a panel of judges who will determine whether or not you get the funding for your startup."

    "Let's see if you will get the funding you need."

    hide brainstorm
    with dissolve
    show presenting
    with dissolve

    "You arrive at the stage anxiously awaiting for the judges to tell you to start."

    "How well do you know the judges?"

    "The amount of research you do about the judges, there is an importance in how you present yourself, but there is a greater importance in where the investor lies on your business idea."

    "Confidence in what you are doing is all you need to grab the attention of the judge."

    menu:
        "Do you remember crucial information for your product, and feel confident enough to show it?"
         
        "No. I forgot most of it!":
            jump short

        "Yes, I remember the details.":
            jump long_or_right

    label long_or_right:

        "That's good, forgetting the details would be disastrous."

        menu:

            "Will you tell every single detail to your investors to make sure they have the full picture? Or will you keep it concise, enticing, and with the right details?"

            "The investors must know everything!":
                jump long

            "No, I need to keep it concise and witty":
                jump right


    label short:

        "You fidget in front of the investors, shrink from their demeanor, and whisper your pitch:"

        "Hey... my name is %(player_name)s and I’m here to uhh..."

        "Present my thingy - my idea, which is..."

        "About helping animals and making the Earth more green - I mean, making bottles that are eco-friendly..."

        "And it helps reduce waste - uhh... plastic waste specifically..."

        "Thanks for hearing me out, how much money can you give me?"
        
        "It seems the investors are all skeptical of your pitch due to your unpreparedness."
        
        "Funding is unlikely."

        "Try to improve your pitch next time by including information and being confident in your speech."

        "The End."
        
        return


    label long:

        "You exude your confidence and posture. Perhaps too much. Like a sleazy real estate agent. You boom your pitch:"

        "Greetings, esteemed investors. I am delighted to have this opportunity to present our environmentally friendly product!"

        "Before I get into that, I want to tell a story, a very sad story when I was a child."

        "It started way back when I saw the dirty mass of plastic trash at the beach..."

        "..."
        
        "Some investors seem disinterested already. You continue your spiel."

        "..."
        
        "And so I had an epiphany when I was drinking from my water bottle at my desk..."
        
        "..."

        "Others have fallen asleep, but you must continue."

        "..."

        "This bottle here will solve all our environmental problems made out of these compounds, which can be produced by..."

        "..."

        "The technical details make the investors relive their boring school days."

        "..."

        "And that’s a wrap! Any questions?"

        "..."

        "It seems all the investors have fallen asleep from your lengthy pitch. Perhaps consider shortening it next time."

        "The End."
        
        return

    label right:

        "You keep your body confident, but not brash. Your speech flows like silk:"

        "Had enough of polluting the environment through the use of plastic water bottles?"

        "Your journey starts now with our environmentally friendly water bottle!"

        "Our bottle is made from biodegradable materials that cuts your carbon footprint, and offers you a sustainable solution to drinking, not to mention the fact that it's also reusable."

        "Our sleek and stylish design comes in a variety of designs and can benefit the environment with style!"

        "Switch to our environmentally friendly water bottle right away to join us in the fight against plastic waste!"

        "The investors are moved by your pitch. You've done a fantastic job! Good thing you've researched how to make a good business plan and pitch!"

        "The End."
        
        return
