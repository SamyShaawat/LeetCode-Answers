class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        ans = []
        changed = True
        while changed:
            changed = False
            for recipe, ingredient in zip(recipes, ingredients):
                if all(ing in supplies for ing in ingredient) and recipe not in supplies:
                    changed = True
                    supplies.add(recipe)
                    ans.append(recipe)
        return ans
        