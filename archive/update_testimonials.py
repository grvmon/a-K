import re

with open('index.html', 'r') as f:
    content = f.read()

# Replace Card 1
card1_old = """                    <!-- Testimonial Card 1 -->
                    <div class="testimonial-card">
                        <div class="testimonial-icon">
                            <i data-feather="trending-up"></i>
                        </div>
                        <div class="testimonial-body">
                            <h4 class="testimonial-quote-title">"I secured a 100% return in just 3 years."</h4>
                            <p class="testimonial-quote-text">
                                "We were hesitant about the initial valuation, but Acre&amp;Key's data-driven micro-market analysis was spot on. Their advice on exit timing and entry pricing helped us double our capital."
                            </p>
                            <div class="testimonial-author">— Rajveer Meena, <em>Entrepreneur</em></div>
                        </div>
                    </div>"""

card1_new = """                    <!-- Testimonial Card 1 -->
                    <div class="testimonial-card">
                        <div class="testimonial-body">
                            <h4 class="testimonial-quote-title">"I secured a 100% return in just 3 years."</h4>
                            <p class="testimonial-quote-text">
                                We were hesitant about the initial valuation, but Acre&amp;Key's data-driven micro-market analysis was spot on. Their advice on exit timing and entry pricing helped us double our capital.
                            </p>
                        </div>
                        <div class="testimonial-author-block">
                            <div class="author-avatar">
                                <img src="https://ui-avatars.com/api/?name=Rajveer+Meena&background=F7F3EC&color=B88E52&size=128" alt="Rajveer Meena">
                            </div>
                            <div class="author-details">
                                <div class="author-name">Rajveer Meena</div>
                                <div class="author-title">Entrepreneur</div>
                            </div>
                            <div class="author-icon">
                                <i data-feather="trending-up"></i>
                            </div>
                        </div>
                    </div>"""

# Replace Card 2
card2_old = """                    <!-- Testimonial Card 2 -->
                    <div class="testimonial-card">
                        <div class="testimonial-icon">
                            <i data-feather="home"></i>
                        </div>
                        <div class="testimonial-body">
                            <h4 class="testimonial-quote-title">"Guided us to invest in a larger home for our growing family."</h4>
                            <p class="testimonial-quote-text">
                                "They didn't just sell us a flat; they looked at our future. Suggesting a larger layout was the best decision for our kids and remote work needs."
                            </p>
                            <div class="testimonial-author">— Vikram Malhotra, <em>Tech CXO</em></div>
                        </div>
                    </div>"""

card2_new = """                    <!-- Testimonial Card 2 -->
                    <div class="testimonial-card">
                        <div class="testimonial-body">
                            <h4 class="testimonial-quote-title">"Guided us to invest in a larger home for our growing family."</h4>
                            <p class="testimonial-quote-text">
                                They didn't just sell us a flat; they looked at our future. Suggesting a larger layout was the best decision for our kids and remote work needs.
                            </p>
                        </div>
                        <div class="testimonial-author-block">
                            <div class="author-avatar">
                                <img src="https://ui-avatars.com/api/?name=Vikram+Malhotra&background=F7F3EC&color=B88E52&size=128" alt="Vikram Malhotra">
                            </div>
                            <div class="author-details">
                                <div class="author-name">Vikram Malhotra</div>
                                <div class="author-title">Tech CXO</div>
                            </div>
                            <div class="author-icon">
                                <i data-feather="home"></i>
                            </div>
                        </div>
                    </div>"""

# Replace Card 3
card3_old = """                    <!-- Testimonial Card 3 -->
                    <div class="testimonial-card">
                        <div class="testimonial-icon">
                            <i data-feather="activity"></i>
                        </div>
                        <div class="testimonial-body">
                            <h4 class="testimonial-quote-title">"Complete focus on lifestyle, elite clubhouse, and amenities."</h4>
                            <p class="testimonial-quote-text">
                                "We wanted a holistic environment. Acre&amp;Key filtered options to show us relevant projects with exceptional open spaces and community infrastructure. We love our active lifestyle here."
                            </p>
                            <div class="testimonial-author">— Priya &amp; Kedar Deshpande, <em>Finance Professionals</em></div>
                        </div>
                    </div>"""

card3_new = """                    <!-- Testimonial Card 3 -->
                    <div class="testimonial-card">
                        <div class="testimonial-body">
                            <h4 class="testimonial-quote-title">"Complete focus on lifestyle, elite clubhouse, and amenities."</h4>
                            <p class="testimonial-quote-text">
                                We wanted a holistic environment. Acre&amp;Key filtered options to show us relevant projects with exceptional open spaces and community infrastructure. We love our active lifestyle here.
                            </p>
                        </div>
                        <div class="testimonial-author-block">
                            <div class="author-avatar">
                                <img src="https://ui-avatars.com/api/?name=Priya+Deshpande&background=F7F3EC&color=B88E52&size=128" alt="Priya & Kedar Deshpande">
                            </div>
                            <div class="author-details">
                                <div class="author-name">Priya &amp; Kedar Deshpande</div>
                                <div class="author-title">Finance Professionals</div>
                            </div>
                            <div class="author-icon">
                                <i data-feather="activity"></i>
                            </div>
                        </div>
                    </div>"""

content = content.replace(card1_old, card1_new)
content = content.replace(card2_old, card2_new)
content = content.replace(card3_old, card3_new)

with open('index.html', 'w') as f:
    f.write(content)
