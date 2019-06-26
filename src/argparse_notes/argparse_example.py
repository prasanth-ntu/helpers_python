# https://www.pythonforbeginners.com/argparse/argparse-tutorial
# https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument


### WILL EDIT AND ADD DOCUMENTATION LATER ###
import argparse
import pdb

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()

ap.add_argument("-d","--detection_test", default="hed_model", type=str, required=False, help='Will be used for ...')
ap.add_argument("-f","--flag", default='True', type=str, required=True)
ap.add_argument("-g", "--gpus", default="0", type=str, required=False, help='GPus to use')
ap.add_argument("-l", "--lst", default=[1], required=False, help="Typing '123' will produce a list of '[1,2,3]'")
ap.add_argument("-t1","--trial_list_1",default=[1,2,3,4,5,6], action='append', type=int, help='Entering this argument will append to default ones. Usage "-t1 1 -t1 t0 -t1 100"')
ap.add_argument("-t2","--trial_list_2",default=[2,4,6,8,10,12], nargs='+', type=int, help='Entering this argument will overwrite default ones. Usage "-t2 1 10 100"')
ap.add_argument("-f1","--freq_list_1",default=["none","alpha","theta"], nargs='+', type=str, help='Entering this argument will overwrite default ones. Usage "-f1 none alpha theta"')

args = vars(ap.parse_args())
print ('args:', args)

flag = args['flag']
detection_test = args['detection_test']
gpus = args['gpus']
lst = args['lst']
trial_list_1 = args['trial_list_1']
trial_list_2 = args['trial_list_2']
freq_list_1 = args['freq_list_1']

flag = True if flag == 'True' else False

print ("flag:", flag)
print ("detection_test:", detection_test)
print ("gpus:", gpus)
print ("lst:", lst)
print ("trial_list_1:", trial_list_1)
print ("trial_list_2:", trial_list_2)
print ("freq_list_1:", freq_list_1)

pdb.set_trace()
