# Intelligent Memory Systems

An intelligent memory system IMS is an adaptive system that receives input from a space and produces a set of objects, or models of the information received from input. This is called framing. When an object is used to frame the input, it is considered active.

Active objects are more likely to be used in framing the input than inactive objects. The active set is limited in size, and when new objects becomes active, the oldest elements are pushed out and become inactive.

Objects become interrelated when they spend time in the active set simultaneously. Objects that are connected to active objects are more likely to become active themselves by placing them in a predicted set. The objects in the predicted set are more easily retrieved, and thus more likely to be used in framing the input set and become active. In doing so, their connections with other objects are reinforced, causing the prediction to occur more often in the future.

When all predictions fail, a local search is conducted by changing the constraints of the filter that controls how information passes between active (short term) and inactive (long term) memory. The restrictions of the filter are lifted to allow more objects to flow into the predicted set, which increases the probability of finding an accurate object to frame the input.

Various goals and objectives change the behavior of the filter. Filters execute scripts, or sets of instructions that define how information should be handled as it passes between short and long term memory. If-then statements define certain objects to trigger operations, allowing the state of the system to influence how the operations of the filter are performed.

Due to the adaptive properties of long term memory in response to short term activity, a filter is applied in order to fit the topology of an object network around the logic of a given script, via function approximation.

A goal is a desired state defined by a set of objects that differ from the active set. A goal influences a filter in the same way as the active set, allowing related information to pass through. The combination of active and goal objects creates a synergistic effect on the activity between the objects to which they’re both related. The result is a predicted set that includes objects connected to both the current and the desired state, providing a potential path between them.

Base filtering is the initial layer of filtering that effects how objects are activated. All activity must reach a certain threshold to become active, and base filtering weighs every activation so that objects become either more difficult or easier to activate and pass through the filter.

First-order filtering applies weights to specific types of objects, determined by the description of objects and their associated weights in a filter script.

Second-order filtering uses conditional rules for determining how objects are weighed, according to current elements in short term memory, which includes the active objects, predicted objects, and/or goal objects.

Filters can be viewed as autonomous agents, performing actions in response to inputs (activated objects) according to a set of decision rules (script logic). Each filter has an of internal memory, which varies in size and complexity based on the needs of the filter.
