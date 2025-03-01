import gpt_2_simple as gpt2

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)

# Print is here because loading the session writes a ton of stuff to the terminal
print('========================\n')

# Length is in characters, temperature is how random (higher is more), prefix is what the comment starts with/replies to
gpt2.generate(sess, length=200, temperature=0.7, prefix="[comment to reply to]")