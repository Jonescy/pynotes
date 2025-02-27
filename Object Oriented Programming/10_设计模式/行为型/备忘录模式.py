"""
定义是：在不破坏封闭的前提下，捕获一个对象的内部状态，并在该对象之外保存这个状态。这样以后就可将该对象恢复到原先保存的状态。简单来说在运行过程中我们可以记录某个状态，当遇到错误时恢复当前状态，这在业务流程中是用设计来处理异常情况。
实际中完整的备忘录应该有三个重要角色：

1.Originator(发起人)：负责创建一个备忘录Memento，用以记录当前时刻自身的内部状态，并可使用备忘录恢复内部状态。Originator可以根据需要决定Memento存储自己的哪些内部状态。

2.Memento(备忘录)：负责存储Originator对象的内部状态，并可以防止Originator以外的其他对象访问备忘录。备忘录有两个接口：Caretaker只能看到备忘录的窄接口，他只能将备忘录传递给其他对象。Originator却可看到备忘录的宽接口，允许它访问返回到先前状态所需要的所有数据。

3.Caretaker(管理者):负责备忘录Memento，不能对Memento的内容进行访问或者操作。
备忘录模式的优点和缺点

一、备忘录模式的优点
1、有时一些发起人对象的内部信息必须保存在发起人对象以外的地方，但是必须要由发起人对象自己读取，这时，使用备忘录模式可以把复杂的发起人内部信息对其他的对象屏蔽起来，从而可以恰当地保持封装的边界。
2、本模式简化了发起人类。发起人不再需要管理和保存其内部状态的一个个版本，客户端可以自行管理他们所需要的这些状态的版本。
3、当发起人角色的状态改变的时候，有可能这个状态无效，这时候就可以使用暂时存储起来的备忘录将状态复原。
二、备忘录模式的缺点：
1、如果发起人角色的状态需要完整地存储到备忘录对象中，那么在资源消耗上面备忘录对象会很昂贵。
2、当负责人角色将一个备忘录 存储起来的时候，负责人可能并不知道这个状态会占用多大的存储空间，从而无法提醒用户一个操作是否很昂贵。
3、当发起人角色的状态改变的时候，有可能这个协议无效。如果状态改变的成功率不高的话，不如采取“假如”协议模式。
"""
import copy


class AddNumber:
    def __init__(self):
        self.start = 1

    def add(self, number):
        self.start += number
        print(self.start)


class Memento:
    """备忘录类"""
    def backups(self, obj=None):
        """
        设置备忘录
        :param obj:
        :return:
        """
        self.obj_dict = copy.deepcopy(obj.__dict__)
        print(f'备忘录数据：{self.obj_dict}')

    def recovery(self, obj):
        """
        恢复备忘录
        :param obj:
        :return:
        """
        obj.__dict__.clear()
        obj.__dict__.update(self.obj_dict)
        return obj


if __name__ == '__main__':
    test = AddNumber()
    memento = Memento()
    for i in [1, 2, 3, 'n', 4]:
        if i == 2:
            memento.backups(test)
        try:
            test.add(i)
        except TypeError as e:
            print(e)
            print(test.start)

    memento.recovery(test)
    print(test.start)
