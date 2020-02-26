#!/usr/bin/env python
# coding: utf-8

# In[2]:


from pymatgen.ext.matproj import MPRester 
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
from pprint import pprint 
with MPRester("B6FsiVusbpLKdMu3") as m:
    structure = m.get_structure_by_material_id("mp-30031")


# In[3]:


sga = SpacegroupAnalyzer(structure)


# In[5]:


# Systeme cristallin
sga.get_crystal_system()


# In[6]:


# Groupe ponctuel
sga.get_point_group_symbol()


# In[7]:


# Type de maille
sga.get_lattice_type()


# In[9]:


# Vecteurs de base du réseau direct
v1 = structure.lattice
print(v1)


# In[10]:


# Vecteurs de base du réseau réciproque 
v2 = structure.lattice.reciprocal_lattice
print(v2)


# In[ ]:




