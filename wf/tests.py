from django.test import TestCase

from model_mommy import mommy

import datetime

# Create your tests here.
from wf.models import Workflow, Node, Task, Transition, Process
from stuff.models import first, second, Order

class TestWorkflows(TestCase):

    def setUp(self):
        fixtures = ['initial_workflow.json']

    def test_ProcessModelSet(self):
        """Tests whether multiple models of undetermined type can be stored and reconstructed from the database"""
        
        # Create a new process instance
        initial_node = Node.objects.get(name="Create Order")
        new_process = Process(current_node=initial_node, date_initiated=datetime.date.today())

        # Create a model set of different models        
        model_set = []
        for i in range(3) :
            model_set.append(mommy.make(first))
            model_set.append(mommy.make(second))
        
        # Write the models to the process record then load them back again
        new_process.write_models(model_set)
        loaded_model_set = new_process.load_models()
        
        # Check that the returned models match the saved models
        for i in range(len(model_set)) :
            self.assertEqual(model_set[i], loaded_model_set[i])
            
    def test_TaskFunctions(self):
        """Task objects store string identifiers for particular functions
             This test checks whether the functions can be read from the database and then executed"""
        
        # Get the Create Order database record
        createOrderTask = Task.objects.get(name="Create Order")
        self.assertTrue(isinstance(createOrderTask, Task))
        
        # Test whether the createOrder function can be executed
        order = Order()
        outcome = createOrderTask.execute([order])
        self.assertEqual(outcome, 1)
        self.assertFalse(order.approved)
        
        # Get the Approve Order record and test whether the approveOrder function
        # can be executed on the object returned by the previous function call
        approveOrderTask = Task.objects.get(name="Approve Order")
        outcome = approveOrderTask.execute([order])
        self.assertTrue(order.approved)
        self.assertFalse(order.received)
        
        # Same again but with the Receive Order task record
        receiveOrderTask = Task.objects.get(name="Receive Order")
        outcome = receiveOrderTask.execute([order])
        self.assertTrue(order.received)
    
    def test_Flow(self):
        """Test whether we can get a process to flow through a workflow"""

        # Create a new order
        order = Order()
        order.save()
        order_id = order.id
        
        # Create a new process
        new_process = Process(current_node=Node.objects.get(name="Create Order"))
        new_process.save()
        new_process.write_models([order])
        new_process.run()
        
        # Check that the order has been processed
        order = Order.objects.get(id=order_id)
        self.assertTrue(order.approved)
        self.assertTrue(order.received)