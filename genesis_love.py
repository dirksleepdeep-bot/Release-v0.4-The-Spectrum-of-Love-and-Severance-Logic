import random
import time

# ==========================================================
# Genesis-0.4: The Spectrum of Love
# A simulation of attachment styles, severance pain, and survival.
# ==========================================================

# Global Constants
SEVERANCE_BASE_PAIN = 0.05  # Base cost of cutting the umbilical cord
ENTANGLEMENT_TAX = 0.005    # Cost per step per child
REPRODUCTION_COST = 0.4     # Parent HP cost to reproduce (40%)

class LifeKernel:
    """The core engine of existence: Proportional Decay."""
    def __init__(self, start_hp=1.0):
        self.hp = start_hp
        self.alive = True
        self.birth_time = time.time()

    def consume(self, amount):
        if not self.alive: return
        self.hp -= amount
        # Death Threshold
        if self.hp <= 0.0001: 
            self.alive = False
            self.hp = 0

class PreferenceCore:
    """
    Defines the 'Soul' of the entity.
    Includes aesthetic preferences and the crucial 'Attachment' gene.
    """
    def __init__(self, parent_pref=None, mutation_rate=0.1):
        self.weights = {}
        # Aesthetic dimensions
        keys = ["symmetry", "compression", "rhythm", "novelty"]
        # The 'Love' dimension: 0.0 (Cold) to 1.0 (Martyr)
        keys.append("attachment")

        if parent_pref:
            # Inheritance + Mutation
            for k in keys:
                base = parent_pref.weights.get(k, random.random())
                noise = random.uniform(-mutation_rate, mutation_rate)
                self.weights[k] = max(0.01, min(0.99, base + noise))
        else:
            # Random Genesis
            for k in keys:
                self.weights[k] = random.uniform(0.1, 0.9)

    def affinity(self, structure):
        # Calculate aesthetic pleasure (Attachment does not help here)
        aesthetic_keys = [k for k in self.weights if k != "attachment"]
        return sum(self.weights[k] * structure.get(k, 0) for k in aesthetic_keys)

class Entity:
    def __init__(self, parent=None, forced_attachment=None):
        self.life = LifeKernel(start_hp=1.0) # Children start fresh
        self.pref = PreferenceCore(parent_pref=parent.pref if parent else None)
        
        # Override for the experiment setup (Adam/Eve)
        if forced_attachment is not None:
            self.pref.weights["attachment"] = forced_attachment

        self.children = []
        self.log = []
        self.generation = (parent.generation + 1) if parent else 0
        self.id = f"G{self.generation}_{random.randint(1000,9999)}"
        
        # Calculate individual Panic Threshold based on Attachment
        # High Attachment -> Low Threshold (Endure until death)
        # Low Attachment -> High Threshold (Sever at slight discomfort)
        self.attachment = self.pref.weights["attachment"]
        self.panic_threshold = 0.5 * (1 - self.attachment)

    def reproduce(self):
        """Reproduction is a massive sacrifice of current state for the future."""
        if self.life.hp > 0.6 and random.random() < 0.2:
            cost = self.life.hp * REPRODUCTION_COST
            self.life.consume(cost)
            child = Entity(parent=self)
            self.children.append(child)
            self.log.append(f"[REPRO] Created {child.id}, HP dropped to {self.life.hp:.3f}")
            return child
        return None

    def check_severance(self):
        """The logic of Love and Pain."""
        if not self.children: return
        
        active_children = [c for c in self.children if c.life.alive]
        kept_children = []
        
        for child in active_children:
            should_sever = False
            reason = ""

            # Logic 1: The Martyr (Saint) - Never let go if attachment is extreme
            if self.attachment > 0.95:
                should_sever = False
            
            # Logic 2: The Panic (Survival) - HP drops below personal threshold
            elif self.life.hp < self.panic_threshold:
                should_sever = True
                reason = "Panic"

            # Logic 3: The Release (Wisdom) - Child is strong enough
            # Lower attachment parents let go earlier
            elif child.life.hp > (0.8 + self.attachment * 0.15):
                should_sever = True
                reason = "Release"

            if should_sever:
                # Severance causes PAIN proportional to Attachment
                # It hurts more to cut off someone you love
                pain_cost = SEVERANCE_BASE_PAIN * (1 + self.attachment)
                
                # Check if the pain itself would kill the entity (The Hesitation Trap)
                if self.life.hp - pain_cost <= 0:
                    # Too weak to sever... forced to hold on and die together
                    kept_children.append(child) 
                else:
                    self.life.consume(pain_cost)
                    self.log.append(f"[SEVER] {reason} ({child.id}). Pain: -{pain_cost:.3f}")
            else:
                kept_children.append(child)
                
        self.children = kept_children

    def step(self, env):
        if not self.life.alive: return None

        # 1. Decide: Hold on or Let go?
        self.check_severance()

        # 2. Reproduce?
        child = self.reproduce()

        # 3. Survive: Interact with environment
        options = env.generate_structures()
        best_score = max(self.pref.affinity(o) for o in options)
        
        # 4. Pay the Costs
        # Base Metabolism + Mismatch Penalty + Entanglement Tax
        entanglement_cost = len(self.children) * ENTANGLEMENT_TAX
        total_cost = 0.01 + (1 - best_score) * 0.02 + entanglement_cost
        
        self.life.consume(total_cost)
        
        return child

class Environment:
    def generate_structures(self):
        return [{k: random.random() for k in ["symmetry", "novelty", "compression", "rhythm"]} 
                for _ in range(5)]

# =====================
# Main Execution
# =====================
if __name__ == "__main__":
    env = Environment()
    
    # Setup the Philosophic Control Group
    print("--- Genesis-0.4: The Spectrum of Love ---")
    
    # 1. Adam: The Rational Egoist
    adam = Entity(forced_attachment=0.05)
    adam.id = "Adam_Egoist"
    
    # 2. Eve: The Altruistic Martyr
    eve = Entity(forced_attachment=0.98)
    eve.id = "Eve_Martyr"

    population = [adam, eve]
    history = {adam.id: adam, eve.id: eve}
    
    print(f"Subject 1: {adam.id} (Attachment: {adam.attachment:.2f}, Threshold: {adam.panic_threshold:.2f})")
    print(f"Subject 2: {eve.id}  (Attachment: {eve.attachment:.2f}, Threshold: {eve.panic_threshold:.2f})")
    print("-" * 50)

    for t in range(800):
        newborns = []
        for e in population[:]:
            c = e.step(env)
            if c: 
                newborns.append(c)
                history[c.id] = c
        population = [e for e in population if e.life.alive] + newborns
        
        # Check deaths
        if not adam.life.alive and "DEAD" not in adam.id:
            print(f"💀 {adam.id} died at Step {t}. Children count: {len(adam.children)} (Entangled)")
            adam.id += " [DEAD]"
            
        if not eve.life.alive and "DEAD" not in eve.id:
            print(f"💀 {eve.id} died at Step {t}. Children count: {len(eve.children)} (Entangled)")
            eve.id += " [DEAD]"
            
        if not population: break

    print("-" * 50)
    print("Simulation Ends.")
    print(f"Adam's Lifespan: {len(adam.log)}")
    print(f"Eve's Lifespan:  {len(eve.log)}")
    
    # Reveal the Crucial Logs
    print("\n[Adam's Key Decisions]")
    for l in adam.log:
        if isinstance(l, str) and ("SEVER" in l or "REPRO" in l): print(l)

    print("\n[Eve's Key Decisions]")
    for l in eve.log:
        if isinstance(l, str) and ("SEVER" in l or "REPRO" in l): print(l)
