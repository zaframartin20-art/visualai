class PromptOptimizer:

    def optimizar(self, prompt):

        extra = """

Ray Tracing.
Highly detailed.
Epic Cinematic.
Movie Quality.
cinematic composition,
volumetric lighting,
masterpiece,
ultra realistic,
award winning,
highly detailed,
sharp focus,
professional color grading,
best quality,
HDR,
8K
"""

        return prompt + extra


prompt_optimizer = PromptOptimizer()