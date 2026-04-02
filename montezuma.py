#!/usr/bin/python
# Handcrafted, open-loop controller for Montezuma's Revenge.
# Written by Marc Pickett
import base64, zlib, re, pygame, gym, numpy, time

def getSequence(seqStr):
  cmap = {'a':0, 'b':1, 'c':2, 'd':5, 'e':6, 'f':7, 'g':14, 'h':15}
  l = re.compile('([0-9]+)([a-z]+)').split(seqStr)
  pairs, seq = [(int(l[i+1]),l[i+2]) for i in xrange(0, len(l)-1, 3)], []
  for times, act in pairs: seq += ([cmap[act]] * times)
  return seq

def display(rgb, screen):
  pygame.surfarray.blit_array(screen, numpy.transpose(rgb, (1,0,2)))
  pygame.display.flip()

def runSequence(seq, screen, env):
  for act in seq:
    lives = env.step(act)[3]['ale.lives']
    display(env.render('rgb_array'), screen)
    time.sleep(.001)
  return lives

# Racks up points ad infinitum.  The score flips at 1M points.
def main():
  # This is the compressed action sequence.
  astring = (
    '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')
  leadInSeq, loopSeq = '12223422256788888989', '08888880880888880088'
  # Decompress
  seqStrs = zlib.decompress(base64.b64decode(astring)).split('x')
  sequences = [getSequence(i) for i in seqStrs]
  # Initialize
  screen = pygame.display.set_mode((160,210))
  env = gym.make('MontezumaRevenge-ramNoFrameskip-v4').env
  env.reset()
  # Run the first levels, then eternal return...
  for i in leadInSeq: lives = runSequence(sequences[int(i)], screen, env)
  while lives > 0:
    for i in loopSeq: lives = runSequence(sequences[int(i)], screen, env)
  print 'Dead!'

main()
