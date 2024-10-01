'''
Modified on Sep 19, 2018
Modified on Sep 18, 2022
@auther: Jingsai
'''
import pytest

import Graph

ga1 = Graph.GraphAlgorithms('graph-1.txt')
ga2 = Graph.GraphAlgorithms('graph-2.txt')
ga3 = Graph.GraphAlgorithms('graph-3.txt')
ga4 = Graph.GraphAlgorithms('graph-4.txt')

def testDFS_recursive():
    assert  ga1.DFS('recursive') == 'abefcgdhij'
    assert  ga2.DFS('recursive') == 'abefcgdhijklmon'
    assert  ga3.DFS('recursive') == 'acdfbeghij'
    assert  ga4.DFS('recursive') == 'abdecf'

def testDFS_stack():
    assert  ga1.DFS('stack') == 'aijdhcgfbe'
    assert  ga2.DFS('stack') == 'aijdhcgfbekmoln'
    assert  ga3.DFS('stack') == 'aefcdbgjih'
    assert  ga4.DFS('stack') == 'acfbed'

def testBFS():
    assert  ga1.BFS() == 'abcdiefghj'
    assert  ga2.BFS() == 'abcdiefghjklmno'
    assert  ga3.BFS() == 'acdefbghji'
    assert  ga4.BFS() == 'abcdef'

def testhasCycle():
    assert ga1.hasCycle()
    assert ga2.hasCycle()
    assert ga3.hasCycle()
    assert not ga4.hasCycle()

## 

